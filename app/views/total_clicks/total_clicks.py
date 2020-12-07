# ------- standard library imports -------
import json
import requests

# ------- 3rd party imports -------
import flask
from flask import Blueprint, render_template, request

total_clicks_blueprint = Blueprint('total_clicks_blueprint', __name__, template_folder='templates')


@total_clicks_blueprint.route('/total_clicks')
def total_clicks():
    new_link = request.args['new_link']

    base_url = flask.url_for("index_blueprint.index", _external=True)
    total_clicks_endpoint = base_url + 'api/total_clicks'

    params = {
        'url': new_link
    }
    response = requests.get(total_clicks_endpoint, params=params)
    total_clicks = json.loads(response.text)['total']
    return render_template('total-clicks.html', total_clicks=total_clicks)
