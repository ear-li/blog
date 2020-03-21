from flask import Flask

from . import modules, routes


def create_app():
    app = Flask('blog')

    app = routes.init_app(app)
    app = modules.init_app(app)

    return app
