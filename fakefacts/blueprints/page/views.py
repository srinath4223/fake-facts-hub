from flask import Blueprint, render_template
from flask_jwt_extended import jwt_optional

page = Blueprint('page', __name__, template_folder='templates')


@page.route('/')
@jwt_optional
def home():
    return render_template('page/home.html')
