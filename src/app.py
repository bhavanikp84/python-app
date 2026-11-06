from flask import Flask, jsonify
from datetime import datetime
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'status': 'ok',
        'message': 'Hello, World!',
    })

@app.route('/api/v1/details')
def details():
    return jsonify({
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'hostname': socket.gethostname(),
        'status': 'ok',
        'message': 'The application is running',
    })


@app.route('/api/v1/healthz')
def healthz():
    return jsonify({
        'status': 'healthy',
        'message': 'The application is running',
    }), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)