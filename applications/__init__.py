import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# создание экземпляра приложения
app = Flask(__name__)
app.config.from_object(os.environ.get('FLASK_ENV') or 'config.TestingConfig')

# инициализирует расширения
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# import views
from . import views
