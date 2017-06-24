from flask import render_template

from app import app

# on / and /index it'd show hello world
@app.route('/')
@app.route('/index')
def index():
	
	
	return render_template("index.html", 
							title='home',)


