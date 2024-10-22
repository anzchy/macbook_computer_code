import mlx_whisper

speech_file = "audio_chunks/chunk_1.mp3"
initial_prompt = "以下是普通话的句子。"  # Use a prompt in Simplified Chinese

# Load and transcribe using the medium model
result = mlx_whisper.transcribe(
    speech_file,
    path_or_hf_repo="mlx_models/base_fp32",
    initial_prompt=initial_prompt,
    language='zh',
    fp16=False
)

# Output transcription
print(result["text"])
