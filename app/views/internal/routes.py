# ------- standard library imports -------
import os

# ------- 3rd party imports -------
from flask import Blueprint, redirect, send_from_directory

# ------- local imports -------
from app.db.db import db
from app.db.models import Url

short_blueprint = Blueprint('short_blueprint', __name__)
app_blueprint = Blueprint('app_blueprint', __name__)


@short_blueprint.route('/<short_url>')
def redirect_to_url(short_url):
    url = Url.query.filter_by(short_url=short_url).first()
    if url:
        url.visits = url.visits + 1
        db.session.commit()
        return redirect(url.original_url)
    return redirect(short_url)


@app_blueprint.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app_blueprint.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
