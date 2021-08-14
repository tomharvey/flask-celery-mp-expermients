from flask import Flask
from bg_queue import start_q_handler

app = Flask(__name__)
queue = start_q_handler()

@app.route('/')
def hello_world():
    queue.put_nowait('Page loaded')
    return 'Hello, World!'
