import os
from flask import Flask, render_template, request, jsonify, send_from_directory
import torch
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image
import pyttsx3

app = Flask(__name__)

# Load the vit-gpt2-image-captioning model and processors
model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
image_processor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

def generate_response(image_path, prompt):
    image = Image.open(image_path).convert("RGB")
    pixel_values = image_processor(images=image, return_tensors="pt").pixel_values
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids

    generated_ids = model.generate(
        pixel_values=pixel_values, input_ids=input_ids, max_length=50, num_beams=4, return_dict_in_generate=True
    )
    generated_text = tokenizer.batch_decode(generated_ids.sequences, skip_special_tokens=True)[0]
    return generated_text

def text_to_speech(text, filename):
    engine = pyttsx3.init()
    engine.save_to_file(text, os.path.join('static', filename))
    engine.runAndWait()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image = request.files['image']
        prompt = request.form['prompt']
        image_path = 'uploaded_image.jpg'
        image.save(image_path)
        response_text = generate_response(image_path, prompt)
        audio_filename = 'output.wav'
        text_to_speech(response_text, audio_filename)
        return jsonify({'response': response_text, 'audio': audio_filename})
    return render_template('index.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)