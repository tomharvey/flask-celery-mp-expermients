from celery import Celery

from bg_queue import start_q_handler
from flask_app import app as flask_app


app = Celery(
    flask_app.import_name,
    broker='redis://localhost:6379'
)

queue = start_q_handler()

@app.task(name='add')
def add(x, y):
    queue.put_nowait('Task run')
    return x + y


if __name__ == '__main__':
    add.delay(1,1)
