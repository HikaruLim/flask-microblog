from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'username':'Hikaru'}
	posts = [
		{
			'author':{'username':'John'},
			'microblog':'Beautiful day in Portland!'
		},
		{
			'author':{'username':'Susan'},
			'microblog':'The Avengers movie was so cool!'
		},
		{
			'author':{'username':'Papi'},
			'microblog':{'today is a good day.'}
		}
	]

	return render_template('index.html',user=user,posts=posts) # no title,default=Welcome

@app.route('/login',methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {},remember_me={}'.format(
			form.username.data,form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html',title='Sign In',form=form)