from flask import Flask, json, request, redirect, jsonify
import os
import urllib.request
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

base_path = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.secret_key = "secret key"

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


app = Flask(__name__)


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/file-upload', methods=['POST'])
def upload_file():

	print(request)

	# check if the post request has the file part
	if 'file' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp
	file = request.files['file']
	if file.filename == '':
		resp = jsonify({'message' : 'No file selected for uploading'})
		resp.status_code = 400
		return resp
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(base_path, filename))
		resp = jsonify({'message' : 'File successfully uploaded'})
		resp.status_code = 201
		return resp
	else:
		resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
		resp.status_code = 400
		return resp


@app.route('/')
def index():
	return f'This is Index Page'


@app.route('/get_data')
def get_data():
	l = ['bob','bill','joe']
	return json.dumps(l)


@app.route('/admin')
def admin():
	return "<h1>you are Admin</h1>"	
