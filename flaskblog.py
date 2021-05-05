from flask import Flask, url_for, render_template
from markupsafe import escape
from forms import RegistrationForm, LoginForm
from flask import flash


# app a Flask class instance
app = Flask(__name__)

app.config['SECRET_KEY'] = '6ee30fca55ef434eb1e0d0401637c1cb'


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

@app.route('/hello/<title>')
def hello(title):
        return render_template('hello.html', name=title)

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
        flash(f'Account created for {form.usrname.data}!', 'success')
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__=='__main__':
    app.run(debug=True)
