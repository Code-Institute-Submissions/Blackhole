import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists('env.py'):
    import env


app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)


@app.route('/')
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("login-username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("login-password")):
                        session["user"] = request.form.get("login-username").lower()
                        flash("Welcome")
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        if request.form.get('password') == request.form.get('confirm-password'):
            # check if username exsists
            existing_user = mongo.db.users.find_one(
                {"username": request.form.get('username').lower()})

            if existing_user:
                flash('Username already exists')
                return redirect(url_for('signup'))

            signup = {
                "first_name": request.form.get('first_name'),
                "last_name": request.form.get('last_name'),
                "username": request.form.get('username').lower(),
                "email": request.form.get('email').lower(),
                "DOB": request.form.get('DOB'),
                "phone_number": request.form.get('phone_number'),
                "password": generate_password_hash(request.form.get('password'))
            }
            mongo.db.users.insert_one(signup)
            # put the user into session
            session['user'] = request.form.get('username').lower()
            flash('Registered Successfully')
            return redirect(url_for('login'))
        else:
            flash('Password Do Not Match!')
    return render_template('signup.html')


@app.route('/support')
def support():
    return render_template('support.html')


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
