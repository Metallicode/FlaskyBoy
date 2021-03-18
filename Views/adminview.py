from applicationsingelton import ApplicationSingelton
import Models.modelimports 
from flask import request
singelton = ApplicationSingelton.instance()

@singelton.app.route('/admin')
def admin():
	return f'this is admin page'
