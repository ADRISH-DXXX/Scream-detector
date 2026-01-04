from flask import Flask, request, jsonify, render_template
import os
from modelloader import process_file
from svm_based_model.model_loader_and_predict import svm_process

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    print("FILE SAVED:", filepath)

    svm_out = svm_process(filepath)
    print("SVM OUTPUT:", svm_out)

    neural_out = process_file(filepath)
    print("NEURAL OUTPUT:", neural_out)

    if svm_out is False and neural_out is False:
        risk = "SAFE"
    elif svm_out is True or neural_out is True:
        risk = "DANGER"
    else:
        risk = "UNCERTAIN"

    print("FINAL RESULT:", risk)
    print("-" * 40)

    return jsonify({"final": risk})

if __name__ == "__main__":
    app.run(debug=True)
