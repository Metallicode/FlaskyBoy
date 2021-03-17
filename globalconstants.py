import os

global_constants_dict = {
    "base_path" : os.path.abspath(os.path.dirname(__file__)),
    "ALLOWED_EXTENSIONS" : set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']),
    "configuration_file":"application.config"

}


