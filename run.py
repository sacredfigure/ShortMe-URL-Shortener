# ------- standard library imports -------
import os

# ------- local imports -------
from app import create_app

CONFIG_FILE = 'settings.py'

app = create_app(config_file=CONFIG_FILE)

production = os.environ.get("PRODUCTION", False)

if __name__ == '__main__':
    app.run()

