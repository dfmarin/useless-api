from flask import Flask, jsonify
import datetime
import socket


app = Flask(__name__)


@app.route('/api/v1/info')
def info():
    return jsonify({
        'env': 'dev',
        'deployed_on': 'kubernetes',
    	'hostname': socket.gethostname(),
        'app_name': 'useless-api',
        'message': "don't worry, everything is working as expected",
    	'time': datetime.datetime.now().strftime("%I:%M:%S%p  on %B %d, %Y"),
        })

# mimic healthz from K8s
# https://kubernetes.io/docs/reference/using-api/health-checks/
@app.route('/api/v1/healthz')
def health():
	# Do an actual check here
    return jsonify({'status': 'up'}), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0")

