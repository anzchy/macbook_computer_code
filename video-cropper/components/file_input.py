import gradio as gr

def create_file_input(label):
    file_input = gr.File(label=label, file_count="single", type="filepath")
    return file_input
