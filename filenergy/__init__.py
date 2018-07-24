from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from filenergy import settings

app = Flask(__name__)

app.secret_key = settings.secret_key
app.config.update(settings.config)

db = SQLAlchemy(app)
db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = settings.login_view

from filenergy import middleware
from filenergy import models
from filenergy import views
from filenergy import admin