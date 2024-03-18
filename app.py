import gradio as gr
print("ciao")
def greet(name):
    return "Hello " + name

demo = gr.Interface(fn = greet, inputs= ["text"], outputs = ["text"])

demo.launch(share = True)
