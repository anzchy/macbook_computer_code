#### You: 

use repo:https://github.com/rany2/edge-tts, to generate audiobook for an epub format file, I want to generate audio for each chapter, but it relates to splitting long text into chunks, generate audio separately and finally merge them for each chapter. please make a thorough analysis of the code package, and write a python script that accept an ePub file as input, and generate an audio. what's more, if the ePub context contains code , you should consider skipping the code, just transcribing the text of each chapter into audio.

#### ChatGPT: 

Alright, here's a plan to fulfill your request of using the `edge-tts` repository to generate an audiobook from an EPUB file, skipping code sections, and ensuring that audio is generated for each chapter individually. I'll begin by making an analysis of the `edge-tts` package and then provide a Python script that takes an EPUB file as input and produces an audio output.Analysis of `edge-tts` RepositoryThe repository `edge-tts` provides a Python implementation to interact with Microsoft Edge's text-to-speech capabilities. It offers an easy-to-use interface for generating audio files directly from a given text using Microsoft's online TTS service.Key points of `edge-tts`: 
1. **Edge-TTS API** : The primary function of the library is to convert text to speech by calling the `Communicate` method.

2. **Features Supported** : 
  - **Voice Selection** : Allows choosing a specific voice or language.

  - **Text Splitting** : Handles chunking the text if it's too long for a single request.

  - **Output Format** : Generates audio files in `.mp3` format.

### Steps to Achieve Your Goal 

1. **Read the EPUB File** : 
  - Parse the EPUB file using `ebooklib` and extract chapter-wise text.

  - Skip the code blocks during the extraction.

2. **Process the Text** :
  - Chunk long text into smaller parts as required by the TTS library.

3. **Use Edge-TTS for Audio Generation** : 
  - Use `edge-tts` to generate audio for each chunk of text.

  - Combine audio chunks for each chapter into a single file.

### Python Script 
Below is a script that reads an EPUB file, extracts each chapter, and generates an audiobook using `edge-tts`.Epub To Audiobook
### Explanation 

1. **Extracting Text** : 
  - The script uses BeautifulSoup to parse each chapter’s HTML content and extracts text while skipping elements that resemble code (using `<code>` tags or keywords like `class`, `def`).

2. **Splitting Text into Chunks** :
  - The text is split into smaller parts (max 3000 characters) to prevent overload issues with TTS.

3. **Generating Audio** : 
  - The `edge-tts` library is used to convert each text chunk into audio files.

  - The generated parts for each chapter are then merged into a single file.

4. **Merging Audio** :
  - The script merges individual audio parts to create a final audio file for each chapter, ensuring continuity.

### Requirements 

- **Libraries** : Install the required libraries using the following commands:

```sh
pip install edge-tts ebooklib beautifulsoup4
```

- **Running the Script** : Replace `"input.epub"` with your EPUB file path and execute the script.

Feel free to adapt the script further based on your specific needs or preferences.

You: 

error:➜ python edge_tts.py
/Users/chengyong/Documents/01_Coding/apps/edge_tts/edge-tts-env/lib/python3.10/site-packages/ebooklib/epub.py:1395: UserWarning: In the future version we will turn default option ignore_ncx to True.
  warnings.warn('In the future version we will turn default option ignore_ncx to True.')
/Users/chengyong/Documents/01_Coding/apps/edge_tts/edge-tts-env/lib/python3.10/site-packages/ebooklib/epub.py:1423: FutureWarning: This search incorrectly ignores the root element, and will be fixed in a future version.  If you rely on the current behaviour, change it to './/xmlns:rootfile[@media-type]'
  for root_file in tree.findall('//xmlns:rootfile[@media-type]', namespaces={'xmlns': NAMESPACES['CONTAINERNS']}):
Traceback (most recent call last):
  File "/Users/chengyong/Documents/01_Coding/apps/edge_tts/edge_tts.py", line 75, in <module>
    epub_to_audio(epub_path, output_dir)
  File "/Users/chengyong/Documents/01_Coding/apps/edge_tts/edge_tts.py", line 62, in epub_to_audio
    asyncio.run(generate_audio(chunks, chapter_output_path))
  File "/opt/homebrew/Cellar/python@3.10/3.10.15/Frameworks/Python.framework/Versions/3.10/lib/python3.10/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/opt/homebrew/Cellar/python@3.10/3.10.15/Frameworks/Python.framework/Versions/3.10/lib/python3.10/asyncio/base_events.py", line 649, in run_until_complete
    return future.result()
  File "/Users/chengyong/Documents/01_Coding/apps/edge_tts/edge_tts.py", line 37, in generate_audio
    communicate = edge_tts.Communicate()
AttributeError: module 'edge_tts' has no attribute 'Communicate'

ChatGPT: 

EditedI've updated the `generate_audio` function to correctly use the `edge_tts.Communicate` class by initializing it with the required parameters (`text` and `voice`) and using the `save()` method to generate the audio files. This should resolve the `AttributeError`. Let me know if you need further adjustments or if you encounter other issues.

You: 

still error:01_Coding/apps/edge_tts via ⬢ v21.1.0 via 🐍 3.10.15 via edge-tts-env via 🅒 base 
➜ python edge_tts.py
/Users/chengyong/Documents/01_Coding/apps/edge_tts/edge-tts-env/lib/python3.10/site-packages/ebooklib/epub.py:1395: UserWarning: In the future version we will turn default option ignore_ncx to True.
  warnings.warn('In the future version we will turn default option ignore_ncx to True.')
/Users/chengyong/Documents/01_Coding/apps/edge_tts/edge-tts-env/lib/python3.10/site-packages/ebooklib/epub.py:1423: FutureWarning: This search incorrectly ignores the root element, and will be fixed in a future version.  If you rely on the current behaviour, change it to './/xmlns:rootfile[@media-type]'
  for root_file in tree.findall('//xmlns:rootfile[@media-type]', namespaces={'xmlns': NAMESPACES['CONTAINERNS']}):
Traceback (most recent call last):
  File "/Users/chengyong/Documents/01_Coding/apps/edge_tts/edge_tts.py", line 76, in <module>
    epub_to_audio(epub_path, output_dir)
  File "/Users/chengyong/Documents/01_Coding/apps/edge_tts/edge_tts.py", line 62, in epub_to_audio
    asyncio.run(generate_audio(chunks, chapter_output_path))
  File "/opt/homebrew/Cellar/python@3.10/3.10.15/Frameworks/Python.framework/Versions/3.10/lib/python3.10/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/opt/homebrew/Cellar/python@3.10/3.10.15/Frameworks/Python.framework/Versions/3.10/lib/python3.10/asyncio/base_events.py", line 649, in run_until_complete
    return future.result()
  File "/Users/chengyong/Documents/01_Coding/apps/edge_tts/edge_tts.py", line 38, in generate_audio
    communicate = edge_tts.Communicate(text=chunk, voice=voice)
AttributeError: module 'edge_tts' has no attribute 'Communicate'

ChatGPT: 

EditedI've modified the `generate_audio` function to correctly use the `Communicate.run` method from `edge_tts`, which is the appropriate method for generating audio from text. This should resolve the `AttributeError`. Please try running the script again and let me know if any other issues arise.

You: 

I have communicate.py in env path:edge-tts-env/lib/python3.10/site-packages/edge_tts/communicate.py, can we import communicate module in the code upfront.

ChatGPT: 

EditedI've updated the code to directly import the `Communicate` class from the `edge_tts.communicate` module. This should resolve any issues related to module importation. Please try running the script again and let me know if you encounter any further errors.



## 从Cursor 获得文件代码后，在VS Code继续编辑

#### You: 

here is the modified version of the python file:

```

import asyncio

import os
import re
from pathlib import Path

import edge_tts
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from pydub import AudioSegment



MAX_CHUNK_LENGTH = 3000  # Maximum characters per chunk
VOICE = "en-US-ChristopherNeural"  # You can change this to your preferred voice

async def text_to_speech(text, output_file):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(output_file)

def remove_code_blocks(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    for code_block in soup.find_all(['code', 'pre']):
        code_block.decompose()
    return str(soup)

def split_text(text):
    chunks = []
    current_chunk = ""
    
    for sentence in re.split(r'(?<=[.!?])\s+', text):
        if len(current_chunk) + len(sentence) <= MAX_CHUNK_LENGTH:
            current_chunk += sentence + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + " "
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

async def process_chapter(chapter, chapter_number, output_dir):
    print(f"Processing Chapter {chapter_number}")
    
    # Remove HTML tags and code blocks
    content = remove_code_blocks(chapter.get_content().decode('utf-8'))
    text = BeautifulSoup(content, 'html.parser').get_text()
    
    # Split text into chunks
    chunks = split_text(text)
    
    # Generate audio for each chunk
    audio_files = []
    for i, chunk in enumerate(chunks):
        output_file = os.path.join(output_dir, f"chapter_{chapter_number}_chunk_{i}.mp3")
        await text_to_speech(chunk, output_file)
        audio_files.append(output_file)
    
    # Merge audio chunks
    merged_audio = AudioSegment.empty()
    for audio_file in audio_files:
        merged_audio += AudioSegment.from_mp3(audio_file)
    
    # Save merged audio
    output_file = os.path.join(output_dir, f"chapter_{chapter_number}.mp3")
    merged_audio.export(output_file, format="mp3")
    
    # Clean up temporary files
    for audio_file in audio_files:
        os.remove(audio_file)

async def epub_to_audio(epub_file, output_dir):
    book = epub.read_epub(epub_file)
    

    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    tasks = []
    for i, item in enumerate(book.get_items_of_type(ebooklib.ITEM_DOCUMENT)):
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            task = asyncio.create_task(process_chapter(item, i, output_dir))
            tasks.append(task)
    
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    epub_file = "Simply_Scheme.epub"
    output_dir = "output"
    

    asyncio.run(epub_to_audio(epub_file, output_dir))
    print("Audio generation complete!")
```
> when running the file, I have encountered errors:➜ python ebook_transcribe.py
/Users/chengyong/Documents/01_Coding/apps/epub_edge_tts/epub-tts-env/lib/python3.10/site-packages/ebooklib/epub.py:1395: UserWarning: In the future version we will turn default option ignore_ncx to True.
  warnings.warn('In the future version we will turn default option ignore_ncx to True.')
/Users/chengyong/Documents/01_Coding/apps/epub_edge_tts/epub-tts-env/lib/python3.10/site-packages/ebooklib/epub.py:1423: FutureWarning: This search incorrectly ignores the root element, and will be fixed in a future version.  If you rely on the current behaviour, change it to './/xmlns:rootfile[@media-type]'
  for root_file in tree.findall('//xmlns:rootfile[@media-type]', namespaces={'xmlns': NAMESPACES['CONTAINERNS']}):
Processing Chapter 0
Processing Chapter 1
Processing Chapter 2
Processing Chapter 3
Processing Chapter 4
Processing Chapter 5
Processing Chapter 6
Processing Chapter 7
Processing Chapter 8
Processing Chapter 9
Processing Chapter 10
Processing Chapter 11
Processing Chapter 12
Processing Chapter 13
Processing Chapter 14
Processing Chapter 15
Processing Chapter 16
Processing Chapter 17
Processing Chapter 18
Processing Chapter 19
Processing Chapter 20
Processing Chapter 21
Processing Chapter 22
Processing Chapter 23
Processing Chapter 24
Processing Chapter 25
Processing Chapter 26
Processing Chapter 27
Processing Chapter 28
Processing Chapter 29
Processing Chapter 30
Processing Chapter 31
Processing Chapter 32
Processing Chapter 33
Processing Chapter 34
Processing Chapter 35
Processing Chapter 36
Processing Chapter 37
Processing Chapter 38
Processing Chapter 39
Processing Chapter 40
Processing Chapter 41
Processing Chapter 42
Processing Chapter 43
Processing Chapter 44
Processing Chapter 45
Processing Chapter 46
Processing Chapter 47
Processing Chapter 48
Processing Chapter 49
Processing Chapter 50
Processing Chapter 51
Processing Chapter 52
Processing Chapter 53
Traceback (most recent call last):
  File "/Users/chengyong/Documents/01_Coding/apps/epub_edge_tts/ebook_transcribe.py", line 90, in <module>
    asyncio.run(epub_to_audio(epub_file, output_dir))
  File "/opt/homebrew/Cellar/python@3.10/3.10.15/Frameworks/Python.framework/Versions/3.10/lib/python3.10/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/opt/homebrew/Cellar/python@3.10/3.10.15/Frameworks/Python.framework/Versions/3.10/lib/python3.10/asyncio/base_events.py", line 649, in run_until_complete
    return future.result()
  File "/Users/chengyong/Documents/01_Coding/apps/epub_edge_tts/ebook_transcribe.py", line 84, in epub_to_audio
    await asyncio.gather(*tasks)
  File "/Users/chengyong/Documents/01_Coding/apps/epub_edge_tts/ebook_transcribe.py", line 63, in process_chapter
    merged_audio += AudioSegment.from_mp3(audio_file)
  File "/Users/chengyong/Documents/01_Coding/apps/epub_edge_tts/epub-tts-env/lib/python3.10/site-packages/pydub/audio_segment.py", line 796, in from_mp3
    return cls.from_file(file, 'mp3', parameters=parameters)
  File "/Users/chengyong/Documents/01_Coding/apps/epub_edge_tts/epub-tts-env/lib/python3.10/site-packages/pydub/audio_segment.py", line 773, in from_file
    raise CouldntDecodeError(
pydub.exceptions.CouldntDecodeError: Decoding failed. ffmpeg returned error code: 183

Output from ffmpeg/avlib:

ffmpeg version 7.1 Copyright (c) 2000-2024 the FFmpeg developers
  built with Apple clang version 15.0.0 (clang-1500.3.9.4)
  configuration: --prefix=/opt/homebrew/Cellar/ffmpeg/7.1 --enable-shared --enable-pthreads --enable-version3 --cc=clang --host-cflags= --host-ldflags='-Wl,-ld_classic' --enable-ffplay --enable-gnutls --enable-gpl --enable-libaom --enable-libaribb24 --enable-libbluray --enable-libdav1d --enable-libharfbuzz --enable-libjxl --enable-libmp3lame --enable-libopus --enable-librav1e --enable-librist --enable-librubberband --enable-libsnappy --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libtesseract --enable-libtheora --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libxvid --enable-lzma --enable-libfontconfig --enable-libfreetype --enable-frei0r --enable-libass --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libspeex --enable-libsoxr --enable-libzmq --enable-libzimg --disable-libjack --disable-indev=jack --enable-videotoolbox --enable-audiotoolbox --enable-neon
  libavutil      59. 39.100 / 59. 39.100
  libavcodec     61. 19.100 / 61. 19.100
  libavformat    61.  7.100 / 61.  7.100
  libavdevice    61.  3.100 / 61.  3.100
  libavfilter    10.  4.100 / 10.  4.100
  libswscale      8.  3.100 /  8.  3.100
  libswresample   5.  3.100 /  5.  3.100
  libpostproc    58.  3.100 / 58.  3.100
[mp3 @ 0x120e30840] Failed to find two consecutive MPEG audio frames.
[in#0 @ 0x120e305f0] Error opening input: Invalid data found when processing input
Error opening input file output/chapter_0_chunk_0.mp3.
Error opening input files: Invalid data found when processing input

---

#### ChatGPT: 

The error you're seeing is related to Pydub failing to process the generated MP3 files, likely because `ffmpeg` is unable to properly decode them. This could happen if the MP3 files are malformed or not properly finalized. Below are the changes and suggestions that could help you resolve the issue:
##### Modifications 

1. **Ensure Proper MP3 Output** : The `edge-tts` library might not properly finalize MP3 files, resulting in issues during decoding. To address this, I will adjust the `generate_audio` function to ensure that files are properly generated and add some error handling.

2. **Add Delay Between Requests** : Sometimes making too many requests in rapid succession might result in incomplete audio files. Introducing a small delay between requests could help.

3. **Adjust Chapter Processing** : Instead of using `asyncio.gather()`, we'll process chapters sequentially to prevent overwhelming the TTS service.

4. **Error Handling** : Add error handling for file processing to catch decoding errors.

Here's an updated version of your script that incorporates these changes:
Edited
I've made several modifications to help resolve the issues with decoding audio files:

1. Introduced a delay (`time.sleep(1)`) between TTS requests to prevent overwhelming the service.

2. Added exception handling to manage errors during audio generation and merging, which should prevent crashes from incomplete files.

3. Updated the merging process to use Pydub with error checking.

Please try running the script again and let me know if these changes help or if further adjustments are needed.

#### You: 

➜ python ebook_transcribe.py
/Users/chengyong/Documents/01_Coding/apps/epub_edge_tts/epub-tts-env/lib/python3.10/site-packages/ebooklib/epub.py:1395: UserWarning: In the future version we will turn default option ignore_ncx to True.
  warnings.warn('In the future version we will turn default option ignore_ncx to True.')
/Users/chengyong/Documents/01_Coding/apps/epub_edge_tts/epub-tts-env/lib/python3.10/site-packages/ebooklib/epub.py:1423: FutureWarning: This search incorrectly ignores the root element, and will be fixed in a future version.  If you rely on the current behaviour, change it to './/xmlns:rootfile[@media-type]'
  for root_file in tree.findall('//xmlns:rootfile[@media-type]', namespaces={'xmlns': NAMESPACES['CONTAINERNS']}):
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 1: [Errno 2] No such file or directory: 'output/chapter_1_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 2: [Errno 2] No such file or directory: 'output/chapter_2_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 3: [Errno 2] No such file or directory: 'output/chapter_3_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 4: [Errno 2] No such file or directory: 'output/chapter_4_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 5: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 5: [Errno 2] No such file or directory: 'output/chapter_5_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 6: [Errno 2] No such file or directory: 'output/chapter_6_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 7: [Errno 2] No such file or directory: 'output/chapter_7_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 5: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 6: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 7: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 8: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 8: [Errno 2] No such file or directory: 'output/chapter_8_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 9: [Errno 2] No such file or directory: 'output/chapter_9_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 10: [Errno 2] No such file or directory: 'output/chapter_10_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 11: [Errno 2] No such file or directory: 'output/chapter_11_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 5: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 6: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 7: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 12: [Errno 2] No such file or directory: 'output/chapter_12_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 5: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 13: [Errno 2] No such file or directory: 'output/chapter_13_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 5: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 6: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 7: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 14: [Errno 2] No such file or directory: 'output/chapter_14_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 5: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 15: [Errno 2] No such file or directory: 'output/chapter_15_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 16: [Errno 2] No such file or directory: 'output/chapter_16_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 5: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 6: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 7: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 8: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 17: [Errno 2] No such file or directory: 'output/chapter_17_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 5: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 18: [Errno 2] No such file or directory: 'output/chapter_18_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 19: [Errno 2] No such file or directory: 'output/chapter_19_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 5: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 6: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 7: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 8: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 9: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 10: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 11: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 12: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 13: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 20: [Errno 2] No such file or directory: 'output/chapter_20_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 21: [Errno 2] No such file or directory: 'output/chapter_21_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 5: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 6: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 7: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 8: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 22: [Errno 2] No such file or directory: 'output/chapter_22_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 5: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 6: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 7: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 8: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 23: [Errno 2] No such file or directory: 'output/chapter_23_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 24: [Errno 2] No such file or directory: 'output/chapter_24_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 5: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 6: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 7: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 8: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 9: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 25: [Errno 2] No such file or directory: 'output/chapter_25_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 26: [Errno 2] No such file or directory: 'output/chapter_26_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 5: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 6: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 27: [Errno 2] No such file or directory: 'output/chapter_27_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 28: [Errno 2] No such file or directory: 'output/chapter_28_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 5: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 6: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 7: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 8: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 9: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 10: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 11: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 12: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 13: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 14: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 15: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 16: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 17: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 18: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 19: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 20: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 21: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 22: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 23: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 29: [Errno 2] No such file or directory: 'output/chapter_29_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 30: [Errno 2] No such file or directory: 'output/chapter_30_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 5: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 6: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 7: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 8: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 9: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 10: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 11: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 12: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 13: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 31: [Errno 2] No such file or directory: 'output/chapter_31_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 5: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 6: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 7: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 8: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 9: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 10: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 32: [Errno 2] No such file or directory: 'output/chapter_32_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 5: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 6: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 33: [Errno 2] No such file or directory: 'output/chapter_33_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 34: [Errno 2] No such file or directory: 'output/chapter_34_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 5: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 6: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 7: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 8: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 9: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 10: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 11: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 12: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 13: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 14: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 15: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 35: [Errno 2] No such file or directory: 'output/chapter_35_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 5: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 6: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 7: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 8: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 36: [Errno 2] No such file or directory: 'output/chapter_36_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 5: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 6: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 7: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 8: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 9: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 10: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 11: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 37: [Errno 2] No such file or directory: 'output/chapter_37_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 5: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 6: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 7: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 8: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 9: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 10: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 11: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 38: [Errno 2] No such file or directory: 'output/chapter_38_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 5: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 6: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 7: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 39: [Errno 2] No such file or directory: 'output/chapter_39_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 5: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 6: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 7: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 8: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 9: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 10: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 11: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 12: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 13: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 14: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 15: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 16: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 17: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 18: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 19: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 20: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 21: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 22: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 40: [Errno 2] No such file or directory: 'output/chapter_40_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 5: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 6: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 7: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 8: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 9: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 10: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 11: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 12: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 41: [Errno 2] No such file or directory: 'output/chapter_41_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 42: [Errno 2] No such file or directory: 'output/chapter_42_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 43: [Errno 2] No such file or directory: 'output/chapter_43_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 44: [Errno 2] No such file or directory: 'output/chapter_44_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 45: [Errno 2] No such file or directory: 'output/chapter_45_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 46: [Errno 2] No such file or directory: 'output/chapter_46_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 5: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 6: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 7: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 8: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 9: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 10: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 47: [Errno 2] No such file or directory: 'output/chapter_47_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 3: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 4: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 5: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 6: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 48: [Errno 2] No such file or directory: 'output/chapter_48_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 49: [Errno 2] No such file or directory: 'output/chapter_49_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 50: [Errno 2] No such file or directory: 'output/chapter_50_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 51: [Errno 2] No such file or directory: 'output/chapter_51_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 52: [Errno 2] No such file or directory: 'output/chapter_52_part0.mp3'
Error generating audio for chunk 0: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 1: Communicate.__init__() missing 1 required positional argument: 'text'
Error generating audio for chunk 2: Communicate.__init__() missing 1 required positional argument: 'text'
Error merging audio for chapter 53: [Errno 2] No such file or directory: 'output/chapter_53_part0.mp3'
Traceback (most recent call last):
  File "/Users/chengyong/Documents/01_Coding/apps/epub_edge_tts/ebook_transcribe.py", line 90, in <module>
    asyncio.run(epub_to_audio(epub_file, output_dir))
  File "/opt/homebrew/Cellar/python@3.10/3.10.15/Frameworks/Python.framework/Versions/3.10/lib/python3.10/asyncio/runners.py", line 37, in run
    raise ValueError("a coroutine was expected, got {!r}".format(main))
ValueError: a coroutine was expected, got None

ChatGPT: 

The issue you're facing seems to be due to incorrect usage of the `Communicate` class from the `edge_tts` library, specifically the instantiation of the `Communicate` object. It expects the text as a parameter, but that wasn't provided in the current script. I will make the necessary adjustments to the code so that the `Communicate` class is instantiated correctly, and ensure the coroutine runs properly with `asyncio`.
Here is the updated version of the code:
EditedI've updated the code to correctly provide the `text` parameter to the `Communicate` class when it is instantiated. This should resolve the issue related to the missing argument. Please try running the script again and let me know if you encounter any further issues.

You: 

The generated text currently feels somewhat stiff. Could it be adjusted so that a complete sentence is input to the TTS API at once for reading? A complete sentence should end with a ".", rather than a "," or a line break or a return.

ChatGPT: 

EditedI've updated the text splitting logic to ensure each chunk ends with a complete sentence if possible. Sentences are split by punctuation (`.`, `!`, `?`) followed by a space, making the text more natural for TTS reading. Let me know if you need further adjustments!

You: 

now it seems to transcribe everything in epub file, add addtion function:after parsing the epub file using ebooklib, can we:1.print out all of the parts it splitted, ordering them in integer numbers2.printout the title and first 30 words of every part into interactive terminal. 3.then the terminal will ask the user which parts to transcribe, it's a multiple choice.4.I will select the numbers( for example "1 3 5", separate by space) of the part that will be transcribed into audio5.then based on my selection, the python script start transcribing into audio

ChatGPT: 

Edited
I've added functionality to list all parts of the EPUB file, display a preview of each part, and allow you to select which parts to transcribe into audio. Let me know if you need further modifications or improvements to the interactive flow!

You: 

error:➜ python ebook_transcribe.py
/Users/chengyong/Documents/01_Coding/apps/epub_edge_tts/epub-tts-env/lib/python3.10/site-packages/ebooklib/epub.py:1395: UserWarning: In the future version we will turn default option ignore_ncx to True.
  warnings.warn('In the future version we will turn default option ignore_ncx to True.')
/Users/chengyong/Documents/01_Coding/apps/epub_edge_tts/epub-tts-env/lib/python3.10/site-packages/ebooklib/epub.py:1423: FutureWarning: This search incorrectly ignores the root element, and will be fixed in a future version.  If you rely on the current behaviour, change it to './/xmlns:rootfile[@media-type]'
  for root_file in tree.findall('//xmlns:rootfile[@media-type]', namespaces={'xmlns': NAMESPACES['CONTAINERNS']}):
The following parts were found in the EPUB file:
Traceback (most recent call last):
  File "/Users/chengyong/Documents/01_Coding/apps/epub_edge_tts/ebook_transcribe.py", line 106, in <module>
    asyncio.run(epub_to_audio(epub_file, output_dir))
  File "/Users/chengyong/Documents/01_Coding/apps/epub_edge_tts/ebook_transcribe.py", line 65, in epub_to_audio
    title = chapter.get_title() if chapter.get_title() else f"Chapter {i}"
AttributeError: 'EpubHtml' object has no attribute 'get_title'. Did you mean: 'get_type'?

ChatGPT: 

EditedI've updated the code to replace `get_title()` with a safe way to access the chapter's title using `chapter.title` if it exists. This should resolve the `AttributeError`. Please try running the updated script and let me know if you encounter any further issues.

You: 

if I choose the number 3-15, will the script knows what i mean: 3 4 5 6 7 … until it ends at 15

ChatGPT: 

The current version of the script only accepts space-separated numbers (e.g., `1 3 5`) to indicate which chapters to transcribe. If you want to be able to specify ranges like `3-15` and have the script understand that as all numbers from 3 to 15 inclusive, I can make the necessary update to accommodate that.I'll add functionality to allow for range input, so you could enter something like `3-15` and it will expand that to `3 4 5 6 ... 15`. I'll also keep the existing space-separated input feature. Here's the updated version:EditedI've updated the script to allow users to input ranges (e.g., `3-15`). The script will now correctly expand those ranges into individual chapter numbers, so you can easily select multiple consecutive parts for transcription. Let me know if there's anything else you'd like to adjust!

You: 

before transcribing after splitting can you output html file of every part separately(the output dir is provided by the user), that is every part has a independent file, rename every file after its chapter name you have given it. then print the first 30 words of every part, then prompt the user to choose.

ChatGPT: 

Edited
I've added functionality to save each chapter as an HTML file, named after its chapter title, and print the first 30 words before prompting the user to select parts for transcription. Let me know if you need further modifications or improvements!

You: 

![Uploaded image](https://files.oaiusercontent.com/file-snEFVIEunsKODkWflldHi5x7?se=2024-10-20T03%3A24%3A37Z&sp=r&sv=2024-08-04&sr=b&rscc=max-age%3D299%2C%20immutable%2C%20private&rscd=attachment%3B%20filename%3Dimage.png&sig=UZ/Qsex9t3WO9wVWJ2KPnGyVFqWCkgjZMnIWexrbNfg%3D) 

seems you have done the rename twice

ChatGPT: 

Epub To Audiobook

999
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
import osimport reimport ebooklibfrom ebooklib import epubfrom bs4 import BeautifulSoupimport asyncioimport timefrom edge_tts import Communicatefrom pydub import AudioSegment
# Function to extract text from EPUB chapters, skipping code blocksdef extract_text_from_chapter(chapter):    soup = BeautifulSoup(chapter.get_body_content(), 'html.parser')    text = ''    for element in soup.find_all(['p', 'div', 'span']):        # Skip code blocks or elements that resemble code        if element.find('code') or re.search(r'\b(class|def|function|var)\b', element.text):            continue        text += element.get_text() + ' '    return text.strip()
# Function to split text into chunks that are manageable by edge-tts# The chunks should end at a complete sentence if possible

EditedI modified the code to only rename the chapter files once, using a cleaned title (`Chapter_{chapter_idx}`). This should prevent the double-renaming issue you observed. Please try running it again and let me know if everything works as expected!

You: 

999
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
import osimport reimport ebooklibfrom ebooklib import epubfrom bs4 import BeautifulSoupimport asyncioimport timefrom edge_tts import Communicatefrom pydub import AudioSegment
# Function to extract text from EPUB chapters, skipping code blocksdef extract_text_from_chapter(chapter):    soup = BeautifulSoup(chapter.get_body_content(), 'html.parser')    text = ''    for element in soup.find_all(['p', 'div', 'span']):        # Skip code blocks or elements that resemble code        if element.find('code') or re.search(r'\b(class|def|function|var)\b', element.text):            continue        text += element.get_text() + ' '    return text.strip()
# Function to split text into chunks that are manageable by edge-tts# The chunks should end at a complete sentence if possible