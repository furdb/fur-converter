from flask import Flask


def create_app():
    app = Flask(__name__)

    from fur_converter.unsigned_integer import unsigned_integer

    app.register_blueprint(unsigned_integer)

    return app
