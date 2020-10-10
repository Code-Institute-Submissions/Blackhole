import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)

from flask_pymongo import PyMongo

from bson.objectid import ObjectId

from werkzeug.security import generate_password_hash, check_password_hash

from datetime import date, datetime

if os.path.exists('env.py'):
    import env

app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)

app.config['cloud_name'] = os.environ.get('cloud_name')

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_date = date_time = now.strftime("%m/%d/%Y")

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
                        return redirect(url_for('home'))
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

            default_settings = {
                'username': session['user'],
                'dark_theme': 'on',
                'light_theme': ''
            }

            mongo.db.user_settings.insert_one(default_settings)

            flash('Registered Successfully')
            return redirect(url_for('home'))
        else:
            flash('Password Do Not Match!')
    return render_template('signup.html')


@app.route('/support')
def support():
    return render_template('support.html')


@app.route('/home', methods=["GET", "POST"])
def home():
    if 'user' not in session:
        flash('You Need To Login First!')
        return redirect(url_for('login'))
    else:
        styles = mongo.db.user_settings.find_one({'username': session['user']})
        if styles.light_theme == '':
#            styles = 'light_theme'
 #       else:
  #          styles = 'dark_theme'
            print(styles)

        posts = list(
            mongo.db.posts.find().sort('date_posted', 1))

        if request.method == 'POST':
            username = mongo.db.users.find_one({'username': session['user']})['username']

            new_post = {
                'description': request.form.get('activity-post'),
                'date_posted': current_date,
                'time_posted': current_time,
                'created_by': username
            }
            mongo.db.posts.insert_one(new_post)
            flash('Posted Successfully!')
            return redirect(url_for('home'))
        return render_template('home.html', posts=posts, styles=styles)


@app.route('/like_post/<post_id>', methods=['GET', 'POST'])
def like_post(post_id):
    mongo.db.posts.find_one_and_update(
        {'_id': ObjectId(post_id)}, {'$inc': {'likes': 1}})

@app.route('/search')
def search():
    if 'user' not in session:
        flash('You Need To Login First!')
        return redirect(url_for('login'))
    else:
        return render_template('search.html')

@app.route('/news_feed')
def news_feed():
    if 'user' not in session:
        flash('You Need To Login First!')
        return redirect(url_for('login'))
    else:
        return render_template('news_feed.html')


@app.route('/notifications')
def notifications():
    if 'user' not in session:
        flash('You Need To Login First!')
        return redirect(url_for('login'))
    else:
        return render_template('notifications.html')


@app.route('/friends')
def friends():
    if 'user' not in session:
        flash('You Need To Login First!')
        return redirect(url_for('login'))
    else:
        return render_template('friends.html')


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if 'user' not in session:
        flash('You Need To Login First!')
        return redirect(url_for('login'))
    else:
    # for the themes add if statements in the base url to check the user settings and display specific css
        if request.method == 'POST':

            settings = {
                'username': session['user'],
                'dark_theme': request.form.get('dark_theme'),
                'light_theme': request.form.get('light_theme')
            }

            mongo.db.user_settings.update({"username": session['user']}, settings)

            flash('Settings Updated')
        return render_template('settings.html')


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
