# ------- standard library imports -------
import json
import unittest

# ------- local imports -------
from app import create_app
from app.db.db import db
from app.db.models import Link


class TestApp(unittest.TestCase):
    VALID_LINK = 'youtube.com'
    INVALID_LINK = 'www.youtube.com/what?a=b&c=d'
    INVALID_PARAM = 'INVALID'

    def setUp(self):
        self.app = create_app(config_file='tests/api_testing/settings.py')

    def test_01_shorten_url_success(self):
        response = self.app.test_client().post(
            '/api/shorten',
            data={'url': self.VALID_LINK},
        )

        res_dict = json.loads(response.get_data(as_text=True))
        self.short_url = res_dict['short_url']
        self.original_url = res_dict['original_url']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(self.short_url), 5)
        self.assertEqual(self.original_url, 'http://youtube.com')

    def test_02_shorten_url_fail(self):
        response = self.app.test_client().post(
            '/api/shorten',
            data={'url': self.INVALID_LINK},
        )

        res_dict = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 404)
        self.assertEqual(res_dict['success'], False)
        self.assertEqual(res_dict['message'], 'could not shorten URL (404)')

    def test_03_total_clicks(self):
        print('02')

        # add link to db
        response = self.app.test_client().post(
            '/api/shorten',
            data={'url': 'youtube.com'},
        )

        with self.app.app_context():
            url = Link.query.filter_by(original_url='http://youtube.com').first()
            short_url = url.short_url

        response = self.app.test_client().get(
            '/api/total_clicks',
            data={'url': short_url},
        )

        res_dict = json.loads(response.get_data(as_text=True))

        self.assertEqual(res_dict['total'], 0)

    def tearDown(self):
        db.session.remove()
        with self.app.app_context():
            db.drop_all()


if __name__ == '__main__':
    unittest.main()
