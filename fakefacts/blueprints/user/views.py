from flask import Blueprint, render_template
from flask_jwt_extended import jwt_required

user = Blueprint('user', __name__, template_folder='templates')


@user.route('/login')
def login():
    return render_template('user/login.html')


@user.route('/signup')
def signup():
    return render_template('user/signup.html')


@user.route('/community')
@jwt_required
def community():
    return render_template('user/community.html')
