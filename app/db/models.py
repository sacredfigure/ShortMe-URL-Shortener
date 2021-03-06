# ------- standard library imports -------
import string
from random import choices
from datetime import datetime

# ------- local imports -------
from .db import db


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    short_url = db.Column(db.String(5), unique=True)
    visits = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_url()

    def generate_short_url(self):
        characters = string.digits + string.ascii_letters
        short_url = ''.join(choices(characters, k=5))
        url = self.query.filter_by(short_url=short_url).first()

        if url:
            return self.generate_short_url()

        return short_url

    def __repr__(self):
        return f'{self.original_url}, {self.visits}'
