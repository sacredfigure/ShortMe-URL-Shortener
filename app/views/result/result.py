# ------- standard library imports -------
import json
import requests

# ------- 3rd party imports -------
import flask
from flask import Blueprint, render_template, request, redirect, url_for

result_blueprint = Blueprint('result_blueprint', __name__, template_folder='templates')


@result_blueprint.route('/add_url', methods=['POST'])
def add_url():
    base_url = flask.url_for("index_blueprint.index", _external=True)
    original_url = request.form['original_url']
    add_url_endpoint = base_url + 'api/shorten'

    params = {
        'url': original_url
    }
    response = requests.post(add_url_endpoint, params=params)

    if response.status_code == 200:
        response = json.loads(response.text)
        new_url = response['short_url']
        original_url = response['original_url']

        return redirect(url_for('result_blueprint.result',
                                new_url=new_url,
                                original_url=original_url))
    else:
        return redirect(url_for('error_blueprint.error'))


@result_blueprint.route('/result')
def result():
    original_url = request.args['original_url']
    new_url = request.args['new_url']
    base_url = flask.url_for("index_blueprint.index", _external=True)
    full_short_url = f'{base_url}{new_url}'
    full_short_url = full_short_url.replace('http://www.', '')

    return render_template('result.html',
                           original_url=original_url,
                           new_url=new_url,
                           full_short_url=full_short_url)
