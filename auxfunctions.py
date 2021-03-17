from globalconstants import global_constants_dict

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in global_constants_dict["ALLOWED_EXTENSIONS"]
