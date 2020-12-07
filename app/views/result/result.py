# ------- standard library imports -------
import json
import requests

# ------- 3rd party imports -------
import flask
from flask import Blueprint, render_template, request, redirect, url_for

result_blueprint = Blueprint('result_blueprint', __name__, template_folder='templates')


@result_blueprint.route('/add_link', methods=['POST'])
def add_link():
    base_url = flask.url_for("index_blueprint.index", _external=True)
    original_url = request.form['original_url']
    add_link_endpoint = base_url + 'api/shorten'

    params = {
        'url': original_url
    }
    response = requests.post(add_link_endpoint, params=params)

    if response.status_code == 200:
        response = json.loads(response.text)
        new_link = response['short_url']
        original_url = response['original_url']

        return redirect(url_for('result_blueprint.result',
                                new_link=new_link,
                                original_link=original_url))
    else:
        return redirect(url_for('error_blueprint.error'))


@result_blueprint.route('/result')
def result():
    original_link = request.args['original_link']
    new_link = request.args['new_link']
    base_url = flask.url_for("index_blueprint.index", _external=True)
    full_short_link = f'{base_url}{new_link}'
    full_short_link = full_short_link.replace('http://www.', '')

    return render_template('result.html',
                           original_link=original_link,
                           new_link=new_link,
                           full_short_link=full_short_link)
