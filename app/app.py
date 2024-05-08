import logging
import logging.config
import os

import yaml
from flask import Flask

app = Flask(__name__)


def setup_logging() -> None:
    if os.environ.get("FLASK_ENV") not in ["development", "production"]:
        raise Exception("FLASK_ENV is not set to dev or prod")
    conf_file = (
        "logging/development.yml"
        if os.environ.get("FLASK_ENV") == "development"
        else "logging/production.yml"
    )
    with open(conf_file, "r") as f:
        conf = yaml.safe_load(f.read())
    logging.config.dictConfig(conf)


setup_logging()


@app.route("/")
def index():
    app.logger.info("Info level log")
    app.logger.debug("Debug level log")
    return "index page"
