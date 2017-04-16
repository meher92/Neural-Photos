from flask import Flask, render_template, json, request, send_from_directory
from flask_pymongo import PyMongo
from app import app

mongo = PyMongo(app)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/<path:filename>')
def send_js(filename):
    return send_from_directory(app.template_folder, filename)