from flask import Flask, render_template, url_for, flash, redirect
from jinja2 import debug
from forms import RegistrationForm, LoginForm
#from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY']='1ad685f672817084afb2404272468465'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite://site.db'

#db=SQLAlchemy(app)

posts= [
    {
        'author':'Nehemiah Cheburet',
        'title':'Blog posting',
        'content': 'first content',
        'date_posted':'January 2019'

    },
    {
        'author':'Nehemiah Limo',
        'title':'Blog posting 2',
        'content': 'end of year',
        'date_posted':'Dec 2018'
    }

]

@app.route('/')
def home():
    return  render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return  redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data=='admin@blog.com' and form.password.data=='pass':
            flash('You have been logged in!', 'success')
            return  redirect(url_for('home'))
        else:
            flash('Login unsuccessfull. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ =='__main__':
    app.run(debug=True)