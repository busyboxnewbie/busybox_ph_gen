from flask import Flask, render_template, request, redirect, url_for, jsonify
# ... other imports

app = Flask(__name__)

# Check and create uploads directory at app startup
import os
UPLOAD_FOLDER = 'static/uploads'  # Define upload folder path
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER # Make it accessible in other parts of your code

# ... your other routes and functions ...

@app.route("/digital_product", methods=["GET", "POST"])
def digital_product():
    if request.method == "POST":
        title = request.form.get("title")
        details = request.form.get("details")
        image = request.files.get("image")  # Line 21 - Correct indentation (4 spaces)
        # ... rest of your code ...
        
# ... rest of your Flask app code
