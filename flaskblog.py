#!/usr/bin/python3
from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfe280ba245'

posts = [
    {'author': 'Kunle Adeniran',
     'title': 'Blog post 1',
     'content': 'First blog post',
     'date_posted': 'Sept 2, 2018'},
    {'author': 'Jane Doe',
     'title': 'Blog post 2',
     'content': 'Second blog post',
     'date_posted': 'Sept 3, 2018'}
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title='About')


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=forms)


if __name__ == '__main__':
    app.run(debug=True)
