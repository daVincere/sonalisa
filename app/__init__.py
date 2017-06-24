from flask import Flask

app = Flask(__name__, static_url_path='/static')
# Also defines the static url path 


# Here app stands for the application, the project that we are on
from app import views