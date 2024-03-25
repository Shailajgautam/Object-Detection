
"""
Simple app to upload an image via a web form 
and view the inference results on the image in the browser.
"""

import io
import os
import shutil
from PIL import Image
import torch
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename

# Load YOLOv5 model
yolov5_model = torch.hub.load('yolov5', 'custom',  path='models/yolov5s.pt',  source='local', force_reload=True)
yolov5_model.eval()

app = Flask(__name__)

# Define the directory for uploading images
UPLOADS_DIR = os.path.join(app.instance_path, 'uploads')

def refresh_paths():
    
    # Create necessary directories for temporary files.
    
    os.makedirs('static/tmp', exist_ok=True)
    clean_path_content('static/tmp')
    os.makedirs('static/tmp/frames', exist_ok=True)
    print(f'Uploading temporary files to {UPLOADS_DIR}')
    os.makedirs(UPLOADS_DIR, exist_ok=True)

def clean_path_content(folder):
    
    # Clean up files in the specified folder.
    
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
            print(f'Files in {folder} deleted')
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

@app.route("/", methods=["GET", "POST"])
def predict():
    
    # Handle image upload and inference requests.
    
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if not file:
            return
        refresh_paths()
        filename = secure_filename(file.filename)
        output_path = os.path.join('static/tmp', filename)
        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes))
        get_img_predictions(img, output_path)
        return redirect(output_path)
    return render_template("index.html")

def get_img_predictions(img, output_path):
    
    # Perform object detection on the input image and save the result.
    
    results = yolov5_model(img, size=640)
    results.render()

    # Save the image with bounding boxes and labels
    img_with_boxes = results.render()[0]  # Render the image with annotations
    img_base64 = Image.fromarray(img_with_boxes)
    img_base64.save(output_path, format="JPEG")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
