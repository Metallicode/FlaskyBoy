from flask import Flask
from globalconstants import global_constants_dict


with open(f"{global_constants_dict['base_path']}/{global_constants_dict['configuration_file']}") as f:
	data = f.read()
	exec(data)

class ApplicationSingelton:
	_instance = None

	def __init__(self):
		raise RuntimeError('Call instance() instead')

	@classmethod
	def instance(cls):
		if cls._instance is None:
			cls._instance = cls.__new__(cls)
			cls._instance.app = Flask(__name__)

		return cls._instance

if __name__ == "__main__":
	app = ApplicationSingelton.instance().app