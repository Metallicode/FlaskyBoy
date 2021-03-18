from flask import Flask, json, request, redirect, jsonify
import urllib.request
from werkzeug.utils import secure_filename
from globalconstants import global_constants_dict
import auxfunctions 
from applicationsingelton import ApplicationSingelton
import Views.views 
import API.applicationapi 

singelton = ApplicationSingelton.instance()
FLASK_APP=singelton.app

@singelton.app.route('/file-upload', methods=['POST'])
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
	if file and auxfunctions.allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(global_constants_dict["base_path"], filename))
		resp = jsonify({'message' : 'File successfully uploaded'})
		resp.status_code = 201
		return resp
	else:
		resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
		resp.status_code = 400
		return resp


