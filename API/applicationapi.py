from applicationsingelton import ApplicationSingelton
import Models.modelimports 
from flask import request, jsonify


singelton = ApplicationSingelton.instance()

@singelton.app.route('/api/file_data')
def file_data():    
	chopstick = {'color': 'bamboo','left_handed': True}
	return jsonify(chopstick)
