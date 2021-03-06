import os
import sys

from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)

from flask_pymongo import PyMongo

from bson.objectid import ObjectId

from werkzeug.security import generate_password_hash, check_password_hash

from datetime import datetime

from cloudinary.api import delete_resources_by_tag, resources_by_tag, cloudinary
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

import random
import string

if os.path.exists('env.py'):
    import env

app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)

cloudinary.config(
  cloud_name=os.environ.get('CLOUD_NAME'),
  api_key=os.environ.get('API_KEY'),
  api_secret=os.environ.get('API_SECRET')
)

DEFAULT_TAG = "blackhole"

now = datetime.now()
current_time = now.strftime("%H:%M")
current_date = now.strftime("%d/%m/%Y")
timeUpload = now.strftime("%H%M%S")
dateUpload = now.strftime('%Y%M%S')
timeDateUpload = "/" + dateUpload + timeUpload


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


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


@app.route('/logout')
def logout():
    flash('You have been logged out!')
    session.pop('user')
    return redirect('login')


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
                "password": generate_password_hash(
                    request.form.get('password'))
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


@app.route('/home', methods=["GET", "POST"])
def home():
    if 'user' not in session:
        flash('You Need To Login First!')
        return redirect(url_for('login'))
    else:
        home = ''
        style = mongo.db.user_settings.find_one(
            {'username': session['user']})['dark_theme']
        if style == 'on':
            home = 'home.html'
        else:
            home = 'light_home.html'

        posts = list(mongo.db.posts.find().sort([('_id', -1)]))

        if request.method == 'POST':
            if request.files['image-post'].filename == '':
                if request.form.get('activity-post') == '':
                    flash('You Need To Add Something To Post!')
                else:
                    username = mongo.db.users.find_one(
                        {'username': session['user']})['username']
                    new_post = {
                        'description': request.form.get('activity-post'),
                        'date_posted': current_date,
                        'time_posted': current_time,
                        'likes': 0,
                        'comments': 0,
                        'photo_id': False,
                        'created_by': username,
                    }

                    mongo.db.posts.insert_one(new_post)
                    flash('Posted Successfully!')
                    return redirect(url_for('home'))
            else:
                username = mongo.db.users.find_one(
                        {'username': session['user']})['username']

                uniqueId = username + timeDateUpload + get_random_string(15)

                cloudinary.uploader.upload(
                    file=request.files.get('image-post'),
                    public_id=uniqueId,
                    quality=100,
                    crop="fill",
                    format='WebP'
                )
                new_post = {
                    'description': request.form.get('activity-post'),
                    'date_posted': current_date,
                    'time_posted': current_time,
                    'likes': 0,
                    'comments': 0,
                    'created_by': username,
                    'photo_id': uniqueId,
                    }

                mongo.db.posts.insert_one(new_post)
                flash('Posted Successfully!')
                return redirect(url_for('home'))

        return render_template(home, posts=posts)


@app.route('/like_post/<post_id>', methods=['GET', 'POST'])
def like_post(post_id):
    mongo.db.posts.find_one_and_update(
        {'_id': ObjectId(post_id)},  {'$inc': {'likes': 1}})
    return redirect(url_for('home'))


@app.route('/all_comments/<post_id>', methods=['GET', 'POST'])
def all_comments(post_id):
    if 'user' not in session:
        flash('You Need To Login First!')
        return redirect(url_for('login'))
    else:
        style = mongo.db.user_settings.find_one(
            {'username': session['user']})['dark_theme']
        if style == 'on':
            all_comments = 'comments.html'
        else:
            all_comments = 'light_comments.html'

        post = mongo.db.posts.find_one({'_id': ObjectId(post_id)})
        str_post_id = str(post_id)

        comments = list(mongo.db.comments.find(
            {'comment_info.comment_for': str_post_id}))

        if request.method == 'POST':
            if request.form.get('comment-post') == '':
                flash('You Need To Add Something To Post!')

            else:
                username = mongo.db.users.find_one(
                    {'username': session['user']})['username']

                new_comment = {'comment_info': {
                    'comment_for': post_id,
                    'comment': request.form.get('comment-post'),
                    'date_posted': current_date,
                    'time_posted': current_time,
                    'created_by': username
                }}

                mongo.db.comments.insert_one(new_comment)

                mongo.db.posts.find_one_and_update(
                    {'_id': ObjectId(post_id)},  {'$inc': {'comments': 1}})

                return redirect(url_for(
                    'all_comments', post_id=post_id))

        return render_template(all_comments, post=post, comments=comments)


@app.route('/delete_comment/<post_id>/<comment_id>/', methods=['GET', 'POST'])
def delete_comment(post_id, comment_id):

    mongo.db.comments.delete_one({'_id': ObjectId(comment_id)})
    print(comment_id)

    return redirect(url_for(
        'all_comments', post_id=post_id, comment_id=comment_id))


@app.route('/delete_post/<post_id>', methods=['GET', 'POST'])
def delete_post(post_id):

    mongo.db.posts.remove({'_id': ObjectId(post_id)})

    return redirect(url_for('home'))


@app.route('/edit_post/<post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    editted_post = {
        'description': request.form.get('edit-description'),
        'date_posted': request.form.get('edit-date'),
        'time_posted': request.form.get('edit-time'),
        'likes': request.form.get('edit-likes'),
        'created_by': request.form.get('edit-username'),
        'photo_id': request.form.get('edit-photo-check'),
    }

    mongo.db.posts.update(
        {'_id': ObjectId(post_id)}, editted_post)

    flash('Post Updated!')
    return redirect(url_for('home'))


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if 'user' not in session:
        flash('You Need To Login First!')
        return redirect(url_for('login'))
    else:
        style = mongo.db.user_settings.find_one(
            {'username': session['user']})['dark_theme']
        if style == 'on':
            settings_html = 'settings.html'
        else:
            settings_html = 'light_settings.html'
        if request.method == 'POST':

            settings = {
                'username': session['user'],
                'dark_theme': request.form.get('dark_theme'),
                'light_theme': request.form.get('light_theme')
            }

            mongo.db.user_settings.update(
                {"username": session['user']}, settings)

            flash('Settings Updated')
            return redirect('settings')
        return render_template(settings_html)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
