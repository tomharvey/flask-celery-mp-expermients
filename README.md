# Flask Celery Multiprocessing

A demo app to explore patterns for MP in flask and celery apps.

This will publish a message to a python multiprocessing
(Queue)[https://docs.python.org/3/library/multiprocessing.html#pipes-and-queues]
when a page is loaded or a task is ran.

When the flask/celery app is started it will also start a
(Process)[https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process]
which will read from the queue. Once it has read the batch size
(which is set to 3 here) it will print the messages it has received
from the queue.

It's the most strpped down version of this pattern. See the
(sentry_sdk)[https://github.com/getsentry/sentry-python]
for a more full featured example.


## Demonstrating the flask app functionality

You should be able to run `gunicorn flask_app:app` to start the flask app.

Then, view the demo page at http://127.0.0.1:8000 and after 3 page loads
it will print the queue contents:

`['Page loaded', 'Page loaded', 'Page loaded']`


## Demonstrating the celery app functionality

You should be able to run `celery -A celery_app worker --loglevel info` to
start a celery worker process.

Then, running `python celery_app.py` will dispatch the `add` task.

After the 3rd execution of a task it will print the queue contents:

`['Task run', 'Task run', 'Task run']`
