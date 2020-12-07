# ------- standard library imports -------
import requests

# ------- 3rd party imports -------
from flask_restful import Resource, reqparse

# ------- local imports -------
from app.db.db import db
from app.db.models import Url

add_url_parser = reqparse.RequestParser()
total_clicks_parser = reqparse.RequestParser()

add_url_parser.add_argument('url', type=str, help='Long URL', required=True)
total_clicks_parser.add_argument('url', type=str, help='Short URL', required=True)


class Shorten(Resource):
    """
    Return a short URL from a given URL
    URL: /api/shorten
    METHOD: POST
    PARAMS: long URL
    RETURN dictionary with the short URL
    """

    @staticmethod
    def post():
        args = add_url_parser.parse_args()
        url = args['url']
        original_url = url if url.startswith('http') else ('http://' + url)

        try:
            res = requests.get(original_url)

            if res.status_code == 200:
                url = Url(original_url=original_url)

                db.session.add(url)
                db.session.commit()

                return dict(
                    short_url=url.short_url,
                    original_url=url.original_url,
                    success=True
                ), 200

            else:
                """in case of 404 response from the URL given"""
                return dict(
                    success=False,
                    message='could not shorten URL (404)'
                ), 404

        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.InvalidURL):
            return dict(
                success=False,
                message='could not shorten URL (404)'
            ), 404


class TotalClicks(Resource):
    """
    return the total clicks of a short URL
    URL: /api/total_clicks
    METHOD: GET
    PARAMS: short url
    RETURN dictionary with the total short url visits {'total': 2}
    """

    @staticmethod
    def get():
        args = total_clicks_parser.parse_args()
        url = args['url'].split('/')[-1]

        try:
            url = Url.query.filter_by(short_url=url).first()

            return dict(
                total=url.visits,
                short_url=url.short_url,
                original_url=url.original_url,
                success=True
            ), 200

        except AttributeError:
            return dict(
                success=False,
                message='could not find the URL (404)'
            ), 404
