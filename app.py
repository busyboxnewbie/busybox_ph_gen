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

@app.route("/product_generator", methods=["GET", "POST"])  # Correct
def product_generator():
    # ... your code ...

@app.route("/digital_product", methods=["GET", "POST"])  # Correct
def digital_product():
    # ... your code ...

        image = request.files.get("image")
        if image:
            filename = image.filename # Keep original filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename) # Use os.path.join for path safety
            image.save(filepath) # Save using the correct path

            image_url = url_for('static', filename='uploads/' + filename) # Generate URL for the image
            # ... rest of your code ...

# ... rest of your Flask app code
