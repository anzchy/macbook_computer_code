import yt_dlp
import os
import time
from queue import Queue
from threading import Thread, Event

# Calculate the number of threads to use (50% of available cores)
MAX_THREADS = max(1, os.cpu_count() // 2)

class VideoDownloader:
    def __init__(self, resolution, progress_callback):
        self.resolution = resolution
        self.progress_callback = progress_callback
        self.download_queue = Queue()
        self.current_download = None
        self.download_results = []
        self.stop_event = Event()

    def add_video(self, video):
        self.download_queue.put(video)

    def download_worker(self):
        while not self.stop_event.is_set():
            if self.current_download is None and not self.download_queue.empty():
                video = self.download_queue.get()
                self.current_download = {
                    'video': video,
                    'start_time': time.time(),
                    'progress': 0
                }

            if self.current_download:
                video = self.current_download['video']
                ydl_opts = {
                    'format': f'bestvideo[height<={self.resolution}]+bestaudio/best[height<={self.resolution}]',
                    'outtmpl': '%(title)s.%(ext)s',
                    'progress_hooks': [self.progress_hook],
                }

                try:
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([video['webpage_url']])
                    self.download_results.append({
                        'title': video['title'],
                        'status': 'Completed',
                        'progress': 100
                    })
                except Exception as e:
                    self.download_results.append({
                        'title': video['title'],
                        'status': f'Failed: {str(e)}',
                        'progress': self.current_download['progress']
                    })

                self.current_download = None

            time.sleep(1)  # Prevent busy-waiting

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            self.current_download['progress'] = float(d['_percent_str'].replace('%', ''))
            elapsed_time = time.time() - self.current_download['start_time']

            if self.current_download['progress'] < 100 and elapsed_time > 600:  # 10 minutes
                self.download_results.append({
                    'title': self.current_download['video']['title'],
                    'status': 'Paused (10 minutes elapsed)',
                    'progress': self.current_download['progress']
                })
                self.current_download = None

            self.progress_callback(d)

    def start_download(self):
        worker_thread = Thread(target=self.download_worker)
        worker_thread.start()

    def stop_download(self):
        self.stop_event.set()

def get_playlist_info(url):
    with yt_dlp.YoutubeDL() as ydl:
        info = ydl.extract_info(url, download=False)
        if 'entries' in info:
            return info['title'], info['entries']
        else:
            return info['title'], [info]

# Export the necessary components
__all__ = ['VideoDownloader', 'get_playlist_info', 'MAX_THREADS']