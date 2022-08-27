#!/usr/bin/env python3
from .flask_config.flask_setup import app
from .flask_config.api_setup import add_resources



if __name__ == '__main__':
    add_resources()
    app.run(debug=True)