from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html", boolean=True)
    #TODO: other examples: text="Testing", user="Wouter"
    

@auth.route('/logout')
def logout():
        return "<p>logout</p>"

@auth.route('/sign-up')
def signup():
    return render_template("signup.html")