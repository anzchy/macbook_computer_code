import sys
import os
from ui import create_interface

# Add the site-packages directory to the Python path
site_packages = '/Users/chengyong/Documents/01_Coding/Cursor_projects/youtube_batch_downloader/yt-download/lib/python3.10/site-packages'
sys.path.append(site_packages)

from ui import create_interface

def main():
    interface = create_interface()
    interface.launch()

if __name__ == "__main__":
    main()