# Flask Celery Multiprocessing

A demo app to explore patterns for MP in flask and celery apps.


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
