import multiprocessing
import gradio

import facefusion.globals
from facefusion.uis.components import about, frame_processors, frame_processors_options, execution, execution_thread_count, execution_queue_count, memory, temp_frame, output_options, common_options, source, target, output, preview, trim_frame, face_analyser, face_selector, face_masker


def pre_check() -> bool:
	return True


def pre_render() -> bool:
	return True

def process_feature2(text_input2, media_input2, choices1, choices2):

	return ""
def render() -> gradio.Blocks:
	with gradio.Blocks() as layout:
		gradio.Markdown("## AUM Live Video Processing App")
		with gradio.Tab("Face Swapper"):
			with gradio.Row():
				with gradio.Column(scale = 2):
					with gradio.Blocks():
						frame_processors.render()
					with gradio.Blocks():
						execution.render()
					with gradio.Blocks():
						output_options.render()
				with gradio.Column(scale = 2):
					with gradio.Blocks():
						source.render()
					with gradio.Blocks():
						target.render()
					with gradio.Blocks():
						output.render()
				with gradio.Column(scale = 3):
					with gradio.Blocks():
						preview.render()
		with gradio.Tab("Generate Video from Text and Media"):
			text_input2 = gradio.Textbox(label="Enter Text")
			with gradio.Row():
				media_input2 = gradio.Video(label="Upload Video or Image")
			with gradio.Row():
				choices1 = gradio.Radio(
					["Prompt A", "Prompt B", "Prompt C"], label="Choose prompt template "
				)
				choices2 = gradio.Radio(
					["Model X", "Model Y", "Model Z"], label="Choose audio model"
				)
			with gradio.Row():    
				generate_button2 = gradio.Button("Generate Video")
				output_video2 = gradio.Video(label="Processed Video")

			generate_button2.click(
				fn=process_feature2,
				inputs=[text_input2, media_input2, choices1, choices2],
				outputs=output_video2,
			)
	return layout


def listen() -> None:
	frame_processors.listen()
	execution.listen()
	output_options.listen()
	source.listen()
	target.listen()
	output.listen()
	preview.listen()


def run(ui : gradio.Blocks) -> None:
	concurrency_count = min(8, multiprocessing.cpu_count())
	ui.queue(concurrency_count = concurrency_count).launch(show_api = False, quiet = True, inbrowser = facefusion.globals.open_browser)
