import os
from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
from encode import encode_image
from decode import decode_image

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
OUTPUT_FOLDER = "static/outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if "file" not in request.files:
        return "❌ No file part"
    
    file = request.files["file"]
    
    if file.filename == "":
        return "❌ No selected file"
    
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        return file_path

@app.route('/encode', methods=['POST'])
def encode():
    image_path = request.form['image_path']
    message = request.form['message']
    output_path = os.path.join(OUTPUT_FOLDER, "stego_image.png")
    
    try:
        encode_image(image_path, message, output_path)
        return f"/{output_path}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

@app.route('/decode', methods=['POST'])
def decode():
    image_path = request.form['image_path']
    try:
        message = decode_image(image_path)
        return message
    except Exception as e:
        return f"❌ Error: {str(e)}"

@app.route('/static/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/static/outputs/<filename>')
def output_file(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)