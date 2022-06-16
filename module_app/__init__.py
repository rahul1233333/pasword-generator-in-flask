from flask import Flask

app = Flask(__name__)

from module_app import views
