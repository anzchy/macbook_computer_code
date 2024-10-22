# use mlx framework developed by Apple, to make the best use of Mac M series chip to perform the transcription.
# Feature: audio chunking, memory management, prompting, when transcribing it will indicates the progress.
# 

import os
import logging
import signal
import gc
from pydub import AudioSegment
import mlx_whisper
from joblib import Parallel, delayed
import resource
from tqdm import tqdm

# Initialize logging
logging.basicConfig(filename='transcription_process.log', level=logging.INFO)

# Set up the MLX Whisper model
# the models are base_fp32, tiny_fp32, small_fp16, but when using fp16, you should specify in the below.
model_path = "mlx_models/base_fp32"
logging.info(f"Using model: {model_path}")

# Audio chunking parameters
CHUNK_LENGTH_MS = 60000  # 1 minute per chunk
OVERLAP_MS = 5000  # 5 seconds overlap

# Set timeout for processing each chunk (in seconds)
CHUNK_TIMEOUT = 120

# Get the current memory limits
soft, hard = resource.getrlimit(resource.RLIMIT_AS)

# Set the new limit to 75% of the current soft limit
MAX_MEMORY_BYTES = int(soft * 0.75)
resource.setrlimit(resource.RLIMIT_AS, (MAX_MEMORY_BYTES, hard))

logging.info(f"Memory limit set to {MAX_MEMORY_BYTES / (1024 * 1024 * 1024):.2f} GB")

def handler(signum, frame):
    raise TimeoutError("Chunk processing took too long")

signal.signal(signal.SIGALRM, handler)

# Hard-coded output format and initial prompt, you can change 
output_format = ".txt" # or ".md", ".srt"
initial_prompt = "以下是英语练习的句子，关键词有英语，人工智能。" 

# Prompt user for language
language ='zh' # e.g., 'zh' for Chinese, 'en' for English

# Load the audio file
audio_path = "english.mp3"
audio_name = os.path.splitext(os.path.basename(audio_path))[0]
audio_dir = os.path.dirname(audio_path)
audio = AudioSegment.from_file(audio_path)

# Create a directory for chunks
if not os.path.exists("audio_chunks"):
    os.makedirs("audio_chunks")

# Split audio into chunks
chunks = []
for i in range(0, len(audio), CHUNK_LENGTH_MS - OVERLAP_MS):
    chunk = audio[i:i + CHUNK_LENGTH_MS]
    chunk_path = f"audio_chunks/chunk_{i // CHUNK_LENGTH_MS}.mp3"
    chunk.export(chunk_path, format="mp3")
    chunks.append((chunk_path, i))

# Function to transcribe a single chunk
def transcribe_chunk(chunk_info):
    chunk_path, start_time = chunk_info
    signal.alarm(CHUNK_TIMEOUT)  # Set timeout alarm for the chunk
    try:
        logging.info(f"Starting transcription for chunk: {chunk_path}")
        result = mlx_whisper.transcribe(
            chunk_path,
            path_or_hf_repo=model_path,
            initial_prompt=initial_prompt,
            language=language,
            fp16=False
        )
        logging.info(f"Completed transcription for chunk: {chunk_path}")
        return result["text"], start_time
    except TimeoutError:
        logging.error(f"Timeout while processing chunk: {chunk_path}")
        return "", start_time
    except Exception as e:
        logging.error(f"Error processing chunk {chunk_path}: {str(e)}")
        logging.exception("Detailed error information:")
        return "", start_time
    finally:
        signal.alarm(0)  # Clear the alarm
        gc.collect()  # Clean up memory

# Process chunks in parallel with progress bar
results = Parallel(n_jobs=4)(delayed(transcribe_chunk)(chunk) for chunk in tqdm(chunks, desc="Transcribing"))

# Combine all results
full_transcription = []
for text, start_time in results:
    full_transcription.append((text, start_time))

# Sort results by start time
full_transcription.sort(key=lambda x: x[1])

# Save the final transcription
def save_transcription(transcription, format, audio_name, audio_dir):
    output_file = os.path.join(audio_dir, f"{audio_name}_transcription{format}")
    with open(output_file, 'w', encoding='utf-8') as f:
        if format == ".srt":
            for idx, (text, start_time) in enumerate(transcription, start=1):
                end_time = start_time + CHUNK_LENGTH_MS
                start_str = f"{start_time//3600000:02d}:{(start_time//60000)%60:02d}:{(start_time//1000)%60:02d},{start_time%1000:03d}"
                end_str = f"{end_time//3600000:02d}:{(end_time//60000)%60:02d}:{(end_time//1000)%60:02d},{end_time%1000:03d}"
                f.write(f"{idx}\n{start_str} --> {end_str}\n{text}\n\n")
        else:
            for text, _ in transcription:
                f.write(f"{text}\n")

save_transcription(full_transcription, output_format, audio_name, audio_dir)

print(f"Transcription saved to {os.path.join(audio_dir, f'{audio_name}_transcription{output_format}')}")