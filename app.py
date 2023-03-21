from flask import Flask, request
from flask.helpers import send_file
from diffusers import StableDiffusionPipeline
import torch




app = Flask(__name__, static_url_path='/', static_folder='web')

@app.route("/")
def indexPage():
    return send_file("web\index.html")


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
    #pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    #pipe = pipe.to("cuda")
    prompt = text
    image = pipe(prompt).images[0]  
    return image
    

