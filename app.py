
import gradio as gr
#import unstructured as us
print("Hello world")
def is_cv(file):
    # pass file through parser
    # pass text to LLM
    response = "Work in"
    return response

title = "CV Scanner"
demo = gr.Interface(fn = is_cv, inputs= [gr.File()], outputs = ["text"], title = title, 
                    description="DISCLAIMER: This is only a Proof-of-Concept demonstration.",
                    article="Please upload the pdf to be scanned.")

demo.queue().launch(share = True)


# with blocks
css = """ h1 {
    text-align: center;
    display:block;} """

with gr.Blocks(css=css) as demo2:
    gr.Markdown("CV Scanner"),
    inputs= [gr.File()],
    outputs = ["text"]
