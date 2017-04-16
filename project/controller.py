import os, time

from flask import Flask, render_template, json, request, send_from_directory

from project import app
import model

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/file_upload_template')
def file_upload_template():
    return render_template('file_upload.html')

@app.route('/upload_image', methods=['POST'])
def caption_image():
    file = request.files['file']
    if file:
        response = model.save_file(file)
    else:
        response = {"error": "No file"}
    return json.dumps(response)

@app.route('/<path:filename>')
def send_js(filename):
    return send_from_directory(app.template_folder, filename)
