from flask import Flask


def create_app():
    app = Flask(__name__)

    from .unsigned_integer import unsigned_integer
    app.register_blueprint(unsigned_integer)

    from .long_string import long_string
    app.register_blueprint(long_string)

    return app
