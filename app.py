from flask import Flask
from prometheus_client import start_http_server, Summary
import random
import time

app = Flask(__name__)

# Create a metric to track request processing time
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@REQUEST_TIME.time()
@app.route('/')
def hello():
    return "Hello, Prometheus!"

@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == '__main__':
    start_http_server(8000)  # Prometheus scraper can scrape this port
    app.run(host='0.0.0.0', port=5000)
