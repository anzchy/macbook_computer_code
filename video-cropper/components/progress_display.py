import gradio as gr

def create_progress_display():
    progress_text = gr.Textbox(label="Progress")
    return progress_text
