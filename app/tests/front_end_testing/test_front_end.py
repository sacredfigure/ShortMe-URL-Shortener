# ------- standard library imports -------
import unittest
import multiprocessing
from time import sleep

# ------- 3rd party imports -------
from selenium import webdriver
from flask_testing import LiveServerTestCase

# ------- local imports -------
from app import create_app
from app.tests.front_end_testing.index.index import Index
from app.tests.front_end_testing.result.result import Result
from app.tests.front_end_testing.total_clicks.total_clicks import TotalClicks


class TestAppSuccess(LiveServerTestCase, unittest.TestCase):
    multiprocessing.set_start_method("fork")

    def create_app(self):
        app = create_app(config_file='tests/api_testing/settings.py')
        app.config.update(LIVESERVER_PORT=8002)
        return app

    @classmethod
    def setUpClass(cls):
        cls.chrome_browser = webdriver.Chrome()

    def test_01_index(self):
        self.chrome_browser.get(self.get_server_url())
        index = Index(self.chrome_browser)

        # test that empty input shows error
        index.click_shorten_button()
        self.assertEqual(index.check_warning_present(), True)

        # test that an invalid link redirecrt to error page
        index.enter_invalid_link()
        index.click_shorten_button()
        self.assertEqual(index.get_current_url(), 'error')
        index.click_try_again()

        # check if heading is present
        heading = index.get_heading_text()
        self.assertEqual(heading,
                         'ShortMe is a free tool to shorten a URL.\nUse our URL Shortener to create a rememberable and easy-to-share URL.')

        # test that a valid URL is working
        index.enter_valid_link()
        index.click_shorten_button()

    def test_02_result(self):
        result = Result(self.chrome_browser)
        # test that the short URL exist inside the input element
        short_url = result.get_input_text()
        self.assertIsNotNone(short_url)

        # test that the copy button works
        result.click_copy_button()
        clipboard_content = result.get_clipboard_content()

        self.assertEqual(clipboard_content, short_url)

        # go to the total_clicks page
        result.go_to_total_clicks()

    def test_03_total_clicks(self):
        total_clicks = TotalClicks(self.chrome_browser)
        sleep(1)
        # test that the text matches the expected
        p_text = total_clicks.get_total_paragraph_text()
        self.assertEqual(p_text, 'Your link has been clicked 0 times so far.')


if __name__ == '__main__':
    unittest.main()
