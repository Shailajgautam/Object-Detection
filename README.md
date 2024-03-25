

# Object Detection Web Application

This is a simple web application for uploading an image via a web form and viewing the inference results on the image in the browser. The application uses the YOLOv5 model for object detection.

## Deployment Instructions

### Step 1: Clone the Repository
Clone the GitHub repository containing the Object Detection application:

```bash
git clone https://github.com/Shailajgautam/Object-Detection.git
cd Object-Detection
```

### Step 2: Clone YOLOv5 Repository
Clone the YOLOv5 repository, which is a submodule of the main repository:

```bash
git clone https://github.com/ultralytics/yolov5.git
```

### Step 3: Install Requirements
Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
Run the Flask application:

```bash
python main.py
```

### Step 5: Access the Application
Open your web browser and navigate to `http://localhost:8080` to access the Object Detection application.

## Additional Notes:
- Ensure that you have Python installed on your system.
- It's recommended to use a virtual environment to isolate project dependencies.
- Make sure the necessary models and files are available in the appropriate directories as specified in the code.
- Adjust the configuration and paths as needed for your specific environment.

---

With these instructions, you should be able to deploy the Object Detection application locally and access it through your web browser.
