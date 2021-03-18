from applicationsingelton import ApplicationSingelton
import Models.modelimports 
from flask import request
singelton = ApplicationSingelton.instance()

@singelton.app.route('/')
def index():
	return f'hello index'
