from flask import Flask, request
from flask.helpers import send_file
from diffusers import StableDiffusionPipeline
import torch
import tempfile




app = Flask(__name__, static_url_path='/', static_folder='web')

@app.route("/")
def indexPage():
    return send_file("web/index.html")


@app.route('/submit', methods=['GET', 'POST'])
def login():
    text = request.args.get('text')
    print(text)
    if (text == ""):
        return "Please use text parameter in GET URL"
    url=getImage(text)
    print(url)
    return send_file(url)

def getImage(text):
    model_id = "runwayml/stable-diffusion-v1-5"
    pipe = StableDiffusionPipeline.from_pretrained(model_id)

    #with a graphics card, use the following codes

    #pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    #pipe = pipe.to("cuda")
    prompt = text
    image = pipe(prompt).images[0]  
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
        image.save(temp_file, format='PNG')
        file_path = temp_file.name
    return file_path
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
