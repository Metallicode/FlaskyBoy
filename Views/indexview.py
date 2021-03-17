from applicationsingelton import ApplicationSingelton
import Models.modelimports 
from flask import request
singelton = ApplicationSingelton.instance()

@singelton.app.route('/')
def index():
	lst = Models.modelimports.Post.query.all()
	#return request.url
	return f'{lst[0].title}  {lst[0].text}  {lst[0].created}'
