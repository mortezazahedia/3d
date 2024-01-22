import os, sys

from flask import render_template, redirect, url_for, flash ,request
from easystudy.forms import Register, Login , Account
from easystudy import app, bcrypt , db
from easystudy.models import add_user, User
from flask_login import login_required,login_user, logout_user, current_user
from PIL import Image


@app.route('/')
@app.route('/home')
def home():
    return render_template('/home.html', title='home')


@app.route('/success')
def success():
    return render_template('/success.html', title='success')


@app.route('/about')
def about():
    return render_template('/about.html', title='home')


@app.route('/posts')
@login_required
def posts():
    return render_template('/post.html', title='post')


@app.route('/add_post')
@login_required
def add_post():
    return render_template('/add_post.html', title='add post')


@app.route('/login', methods=['GET', 'POST'])
def login():
    Loginform = Login()
    if Loginform.validate_on_submit():
        result = User.query.filter_by(email=Loginform.email.data).first()
        if result and bcrypt.check_password_hash(result.password, Loginform.password.data):
            login_user(result,remember=Loginform.remember.data )
            flash("login was Successfull!", "success")
            return redirect(url_for('posts'))
        else:
            flash("Password is wrong", "danger")
            return render_template('/login.html', title='login', tmp_login=Loginform)
    #else:
    #    flash("login was UnSuccessfull!", "danger")
    return render_template('/login.html', title='login', tmp_login=Loginform)


@app.route('/register', methods=['GET', 'POST'])
def register():
    registerform = Register()
    if registerform.validate_on_submit():
        add_user(registerform)
        flash("Registration was successfull")
        return redirect(url_for('login'))
        # return redirect(url_for('success'))
    return render_template('/register.html', title='register', tmp_registerform=registerform)


@app.route("/logout")
@login_required
def logout():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))

def save_profile_pic(picture):
    filename = picture.filename
    _name, _ext = os.path.splitext(filename)
    newname = bcrypt.generate_password_hash(_name).decode('utf-8')
    newname = newname[0:10] + _ext

    size = 128, 128
    im = Image.open(picture)
    im.thumbnail(size)
    _path = os.path.join(app.root_path, 'static/media/profile_pics',newname)
    im.save(_path)

    return newname

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form=Account()
    if request.method == "GET":
        form.name.data = current_user.name
        form.age.data = current_user.age
        form.email.data = current_user.email
        #form.profile_pic.data=current_user.profile_pic  #No Need
    elif form.validate_on_submit():
        current_user.name = form.name.data
        current_user.age = form.age.data
        current_user.email = form.email.data
        print(form.profile_pic.data)
        #current_user.profile_pic=form.profile_pic.data
        if form.profile_pic.data :
            current_user.profile_pic = '333333.jpeg'
            file_name = save_profile_pic(form.profile_pic.data)
            current_user.profile_pic = file_name
        else:
            current_user.profile_pic = '123.jpeg'
        db.session.commit()
        flash("Your account detailes updated successfully" , "success")
        return redirect(url_for('account'))

    return render_template('/account.html', title='User Account',form=form)