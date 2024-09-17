import gradio as gr
from components import file_input, time_range_picker, crop_button, progress_display
from utils import ffmpeg_utils

def crop_video(video_path, start_time, end_time):
    try:
        output_path, detailed_log = ffmpeg_utils.crop_video(video_path, start_time, end_time)
        return output_path, detailed_log
    except Exception as e:
        return None, gr.Error(str(e))

# Create the Gradio interface
with gr.Blocks() as app:
    gr.Markdown("# Video Cropping App")
    
    with gr.Row():
        video_file = file_input.create_file_input("Choose video")
        time_range = time_range_picker.create_time_range_picker()
    
    crop_btn = crop_button.create_crop_button("Start cropping")
    progress_text = progress_display.create_progress_display()
    
    crop_output = gr.Video()
    
    crop_btn.click(fn=crop_video, inputs=[video_file, time_range[0], time_range[1]], outputs=[crop_output, progress_text])
    
    app.launch()
