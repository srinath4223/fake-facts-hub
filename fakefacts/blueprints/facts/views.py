from flask import Blueprint, render_template, redirect, request, url_for
from flask_jwt_extended import (
    jwt_required,
    current_user
)

facts = Blueprint('facts', __name__, template_folder='templates')


@facts.route('/facts/')
@jwt_required
def index():
    username = request.args.get('username', default=None, type=str)

    if username is None:
        return redirect(url_for('facts.index', username=current_user.username))

    return render_template('facts/index.html')
