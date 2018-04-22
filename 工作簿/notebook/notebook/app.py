# coding = utf-8

from flask import Flask, render_template
from notebook.config import configs
from notebook.models import db


def register_blueprint(app):
    from .handlers import front, course, admin
    app.register_blueprint(front)
    app.register_blueprint(course)
    app.register_blueprint(admin)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)
    register_blueprint(app)

    return app
