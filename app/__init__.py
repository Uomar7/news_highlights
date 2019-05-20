from flask import Flask
from .config import DevConfig

#initializing the application
app = Flask(__name__,instance_relative_config=True)
from flask_bootstrap import Bootstrap

# setting up the configurations
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

bootstrap = Bootstrap(app)

from app import views