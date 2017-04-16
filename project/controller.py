from flask import Flask, render_template, json, request, send_from_directory, jsonify

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
    file_path = request.files['file']
    if file_path:
        response = model.save_file(file_path)
    else:
        response = {"error": "No file"}
    return json.dumps(response)

@app.route('/<path:filename>')
def send_js(filename):
    return send_from_directory(app.template_folder, filename)

@app.route('/uploaded_images/<path:filename>')
def send_img(filename):
    return send_from_directory(app.config['image_upload_path'], filename)

@app.route('/get_page_data', methods=['POST'])
def get_page_data():
    last_image_index = request.json.get('last_image_index', None)
    if not last_image_index:
        last_image_index = 0

    response = {}
    albums = model.get_albums(last_image_index)
    if not albums:
        return jsonify({})
    error = albums[0].get('error', None)
    if not error:
        response['images'] = albums
        response['last_image_index'] = last_image_index+10
        return jsonify(response)
    return jsonify(albums[0])
