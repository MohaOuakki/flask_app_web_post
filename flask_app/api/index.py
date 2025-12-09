from flask_app import app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Response

def handler(environ, start_response):
    return app(environ, start_response)
