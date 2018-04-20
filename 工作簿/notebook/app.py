# coding = utf-8

from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

app.config.update(dict(

))