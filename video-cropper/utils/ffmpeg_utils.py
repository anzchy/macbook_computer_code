import ffmpeg
import sys
import os

def convert_time_to_ffmpeg(time_str):
    """
    Convert a time string in the format "HH:MM:SS" to a FFmpeg-compatible time format.
    """
    hours, minutes, seconds = map(int, time_str.split(':'))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

def crop_video(video_path, start_time, end_time):
    start_time = convert_time_to_ffmpeg(start_time)
    end_time = convert_time_to_ffmpeg(end_time)
    
    output_path = "output.mp4"
    
    # Delete the output file if it exists
    if os.path.exists(output_path):
        os.remove(output_path)
    
    # Print the FFmpeg command for debugging
    print(f"Running FFmpeg command: ffmpeg -i {video_path} -ss {start_time} -to {end_time} -c:v libx264 -c:a aac {output_path}")
    
    try:
        stream = ffmpeg.input(video_path)
        video_stream = stream.video.trim(start=start_time, end=end_time).setpts('PTS-STARTPTS')
        audio_stream = stream.audio.filter('atrim', start=start_time, end=end_time).filter('asetpts', 'PTS-STARTPTS')
        
        output, error = (
            ffmpeg
            .output(video_stream, audio_stream, output_path, vcodec='libx264', acodec='aac')
            .run(capture_stdout=True, capture_stderr=True)
        )
        detailed_log = f"FFmpeg Output:\n{output.decode('utf-8')}\n\nFFmpeg Error:\n{error.decode('utf-8')}"
    except ffmpeg.Error as e:
        detailed_log = f"FFmpeg error: {e.stderr.decode('utf-8')}"
    
    return output_path, detailed_log
