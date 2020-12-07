# ------- 3rd party imports -------
from flask import Flask
from flask_restful import Api

# ------- local imports -------
from app.db.db import db

# ------- local imports -------
from app.views.index.index import index_blueprint
from app.views.internal.routes import short_blueprint
from app.views.result.result import result_blueprint
from app.views.total_clicks.total_clicks import total_clicks_blueprint
from app.views.error.error import error_blueprint
from app.views.internal.routes import app_blueprint

from app.api.api import Shorten, TotalClicks


def create_app(config_file):
    """
    Creating and returning the app
    """

    app = Flask(__name__)
    api = Api(app)
    app.config.from_pyfile(config_file)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    api.add_resource(Shorten, '/api/shorten')
    api.add_resource(TotalClicks, '/api/total_clicks')

    app.register_blueprint(index_blueprint)
    app.register_blueprint(short_blueprint)
    app.register_blueprint(result_blueprint)
    app.register_blueprint(total_clicks_blueprint)
    app.register_blueprint(error_blueprint)
    app.register_blueprint(app_blueprint)
    return app
