from flask import Flask
import sys

from setting import HOST, PORT


def create_app():
    app = Flask('blog')

    from api.version import version

    app.register_blueprint(version)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host=HOST, port=PORT)
