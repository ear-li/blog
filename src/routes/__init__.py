from .version import version

def init_app(app):
    app.register_blueprint(version)

    return app