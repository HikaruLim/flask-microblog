from flask import render_template,flash,redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'username':'Hikaru'}
	posts = [
		{
			'author':{'username':'John','age':23,'level':4},
			'microblog':'Beautiful day in Portland!'
		},
		{
			'author':{'username':'Susan','age':21,'level':2},
			'microblog':'The Avengers movie was so cool!'
		},
		{
			'author':{'username':'Papi','age':31,'level':2},
			'microblog':'today is a good day.'
		}
	]

	return render_template('index.html',user=user,posts=posts) # no title,default=Welcome

@app.route('/login',methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		# flash 里边的参数是什么意思？
		flash('Login requested for user {}, remember_me={}'.format(
			form.username.data,form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html',title='Sign In',form=form)