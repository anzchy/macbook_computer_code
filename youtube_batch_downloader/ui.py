import gradio as gr
from downloader import VideoDownloader, get_playlist_info, MAX_THREADS
import time

def create_interface():
    with gr.Blocks() as interface:
        gr.Markdown("# YouTube Playlist Downloader")
        gr.Markdown(f"(Using {MAX_THREADS} threads to optimize CPU usage)")
        with gr.Row():
            url_input = gr.Textbox(label="YouTube Playlist URL")
            resolution_input = gr.Dropdown(
                choices=["144", "240", "360", "480", "720", "1080"],
                label="Max Resolution",
                value="720"
            )
        info_button = gr.Button("Get Info")
        info_output = gr.Textbox(label="Video/Playlist Info", lines=10)
        download_button = gr.Button("Download")
        download_output = gr.Textbox(label="Download Status", lines=10)
        result_output = gr.Dataframe(
            headers=["Title", "Status", "Progress"],
            label="Download Results"
        )

        def info_callback(url):
            yield "Parsing playlist... This may take a moment for large playlists."
            playlist_title, videos = get_playlist_info(url)
            info = f"Playlist: {playlist_title}, {len(videos)} videos\n\n"
            for idx, video in enumerate(videos, 1):
                info += f"{idx}. {video['title']}\n   URL: {video['webpage_url']}\n\n"
            yield info

        def download_callback(url, resolution):
            progress_output = ""
            def progress_hook(d):
                nonlocal progress_output
                if d['status'] == 'downloading':
                    progress_output = f"Downloading: {d['filename']}\n"
                    progress_output += f"Progress: {d['_percent_str']}\n"
                    progress_output += f"Speed: {d['_speed_str']}\n"
                    progress_output += f"ETA: {d['_eta_str']}\n\n"
                    download_output.update(progress_output)

            playlist_title, videos = get_playlist_info(url)
            downloader = VideoDownloader(resolution, progress_hook)

            for video in videos:
                downloader.add_video(video)

            downloader.start_download()
            
            while downloader.download_queue.qsize() > 0 or downloader.current_download is not None:
                time.sleep(1)
                result_output.update(downloader.download_results)

            downloader.stop_download()
            return "Download completed. Check the results below."

        info_button.click(info_callback, inputs=[url_input], outputs=[info_output])
        download_button.click(download_callback, inputs=[url_input, resolution_input], outputs=[download_output])

    return interface