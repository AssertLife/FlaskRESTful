#!flask/bin/python
from flask import Flask, jsonify
import psutil, getpass

app = Flask(__name__)

def get_computer_info():
	return jsonify(
					suser_name=getpass.getuser(),

					cpu_freq=psutil.cpu_freq().current,
					cpu_percent=psutil.cpu_percent(),

					ram_usage_percent=psutil.virtual_memory().percent,
					since_last_boot=psutil.boot_time(),

					disk_usage_c_percent=psutil.disk_usage("C:\\").percent,
					disk_usage_e_percent=psutil.disk_usage("E:\\").percent
				  )


@app.route('/')
def index():
    return "Hello there, you've reached {}'s Computer:)".format(os.getenv('USERNAME'))

@app.route('/computer_info')
def computerinfo():
	return get_computer_info()


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', debug=True)