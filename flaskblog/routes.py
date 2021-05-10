from flask import url_for, render_template
from flaskblog.forms import RegistrationForm, LoginForm
from markupsafe import escape
from flask import flash, redirect

from flaskblog import app, db, bcrypt
from flaskblog.models import User, Post


posts=[
        {   'author': 'Qi Zhi Li',
            'title': 'what is the title for Q.Z.',
            'content': 'this is the first webpage I made',
            'date_posted': '02/May/2021'
        },
        {   'author': 'Cheedge Lee',
            'title': 'what is the title for Cheedge',
            'content': '2nd webpage content',
            'date_posted': '02/May/2021'
        }
        ]

# route decorator: add aditional functionality
#                   to func
#@app.route("/")
#def hello():
#    return "Hello World"

@app.route('/')
def index():
        return 'Index Page'
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/hello/<name>')
def hello(name):
        return render_template('hello.html', name=name)

@app.route('/user/<username>')
def profile(username):
    # show the user profile for that user
    return '<h1>{} \'s profile</h1>'.format(escape(username))


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return '<h1>Post id is {:d}'.format(post_id)

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

@app.route('/about')
def about():
    return render_template('home.html', title='About')



@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.passwd.data).decode('utf-8')
        user = User(username=form.usrname.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        #flash(f'Account created for {form.usrname.data}!', 'success')
        flash('Account create success, you are able to login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'flask@blog.com' and form.passwd.data == '123':
            flash('you have login success')
            return redirect(url_for('home'))
        else:
            flash('unsuccess, check it', 'danger')
    return render_template('login.html', title='Login', form=form)


