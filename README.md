# Flask Celery Multiprocessing

A demo app to explore patterns for MP in flask and celery apps.


## Starting the flask app

You should be able to run `gunicorn flask_app:app` to start the flask app.

Then, view the demo page at http://127.0.0.1:8000 and after 3 page loads
you should see `['Page loaded', 'Page loaded', 'Page loaded']` logged in
the console.


