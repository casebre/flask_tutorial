from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
	user_name = {'nickname': 'Casebre'} 
	posts = [
		{
			'author': {'nickname': 'Jao'},
			'body': 'Beatiful day in Portland'
		},
		{
			'author': {'nickname': 'Susan'},
			'body': 'The Avengers movie was so cool'
		}
	]
	return render_template(
			  'index.html',
			  title = 'Main',
			  user=user_name,
			  posts=posts
			)

@app.route('/about')

def about():
	return render_template(
			'about.html',
			title = 'About'
			)
