# coding = utf-8
from flask import Flask, render_template
from flask_login import LoginManager
from notebook.config import configs
from notebook.models import db, User, Work


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)
    register_blueprint(app)
    register_extensions(app)

    return app


def register_blueprint(app):
    from .handlers import front, work, admin
    app.register_blueprint(front)
    app.register_blueprint(work)
    app.register_blueprint(admin)


def register_extensions(app):
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(user_id):
        return User.query.get(user_id)

    login_manager.login_view = 'front.login'
