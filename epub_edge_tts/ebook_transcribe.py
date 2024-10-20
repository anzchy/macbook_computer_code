import os
import re
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import asyncio
import time
from edge_tts import Communicate
from pydub import AudioSegment

# Function to extract text from EPUB chapters, skipping code blocks
def extract_text_from_chapter(chapter):
    soup = BeautifulSoup(chapter.get_body_content(), 'html.parser')
    text = ''
    for element in soup.find_all(['p', 'div', 'span']):
        # Skip code blocks or elements that resemble code
        if element.find('code') or re.search(r'\b(class|def|function|var)\b', element.text):
            continue
        text += element.get_text() + ' '
    return text.strip()

# Function to split text into chunks that are manageable by edge-tts
# The chunks should end at a complete sentence if possible
def split_text_into_chunks(text, max_length=3000):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    current_chunk = ""
    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= max_length:
            current_chunk += sentence + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + " "
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

# Function to save chapter content to an HTML file
def save_chapter_to_html(chapter_text, title, output_dir, chapter_idx):
    title_cleaned = f"Chapter_{chapter_idx}"
    html_content = f"<html><head><title>{title}</title></head><body><h1>{title}</h1><p>{chapter_text}</p></body></html>"
    output_file = os.path.join(output_dir, f"{title_cleaned}.html")
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_content)

# Async function to generate audio using edge-tts
async def generate_audio(chunks, output_path, voice="en-US-JennyNeural"):
    for idx, chunk in enumerate(chunks):
        try:
            communicate = Communicate(text=chunk, voice=voice)
            output_file = f"{output_path}_part{idx}.mp3"
            await communicate.save(output_file)
            # Adding delay to ensure the service is not overwhelmed
            time.sleep(1)
        except Exception as e:
            print(f"Error generating audio for chunk {idx}: {e}")

# Main function to convert EPUB to audio
def epub_to_audio(epub_path, output_dir):
    # Load the EPUB book
    book = epub.read_epub(epub_path)
    chapters = [item for item in book.get_items() if item.get_type() == ebooklib.ITEM_DOCUMENT]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Print out all of the parts
    print("The following parts were found in the EPUB file:")
    for i, chapter in enumerate(chapters):
        chapter_text = extract_text_from_chapter(chapter)
        if not chapter_text.strip():
            continue
        title = f"Chapter {i+1}"
        preview = ' '.join(chapter_text.split()[:30])
        # Save chapter content to HTML file
        save_chapter_to_html(chapter_text, title, output_dir, i + 1)
        print(f"{i + 1}: {title} - {preview}...")

    # Prompt user for selection
    selected_parts_input = input("Enter the numbers of the parts you want to transcribe (e.g., '1 3 5' or '3-15'): ")
    selected_parts = []
    for part in selected_parts_input.split():
        if '-' in part:
            start, end = map(int, part.split('-'))
            selected_parts.extend(range(start, end + 1))
        else:
            selected_parts.append(int(part))

    for chapter_idx in selected_parts:
        chapter = chapters[chapter_idx - 1]
        # Extract text from the chapter
        chapter_text = extract_text_from_chapter(chapter)
        if not chapter_text.strip():
            continue

        # Split the chapter text into manageable chunks
        chunks = split_text_into_chunks(chapter_text)

        # Generate audio for each chunk
        chapter_output_path = os.path.join(output_dir, f"chapter_{chapter_idx}")
        asyncio.run(generate_audio(chunks, chapter_output_path))

        # Merge audio parts for the chapter into one file
        try:
            merged_audio = AudioSegment.empty()
            for idx in range(len(chunks)):
                part_file = f"{chapter_output_path}_part{idx}.mp3"
                audio_segment = AudioSegment.from_mp3(part_file)
                merged_audio += audio_segment
                os.remove(part_file)  # Clean up part file after merging

            # Export the merged audio
            merged_audio.export(f"{chapter_output_path}.mp3", format="mp3")
        except Exception as e:
            print(f"Error merging audio for chapter {chapter_idx}: {e}")



if __name__ == "__main__":
    epub_file = "Naval.epub"
    output_dir = "audio"
    
    asyncio.run(epub_to_audio(epub_file, output_dir))
    print("Audio generation complete!")