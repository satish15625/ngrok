from flask import Flask
import subprocess
from subprocess import Popen

app = Flask(__name__)
# run_with_ngrok(app)  # Start ngrok when app is run

@app.route('/run')
def runbat():
	pipe = subprocess.Popen(["bash", "run.sh"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, errors = pipe.communicate()
	pipe.wait()
	return output

if __name__ == '__main__':
	app.run(host = '127.0.0.1', port = 5000, debug = True)
