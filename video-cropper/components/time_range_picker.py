import gradio as gr

def create_time_range_picker():
    start_time = gr.Textbox(label="Start", placeholder="00:00:00")
    end_time = gr.Textbox(label="End", placeholder="00:00:00")
    return start_time, end_time
