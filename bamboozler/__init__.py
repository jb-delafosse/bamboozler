import os

from flask import Flask

APP = Flask(__name__)
APP.config.from_object("bamboozler.default_settings")
APP.config.from_envvar("BAMBOOZLER_SETTINGS")

if not APP.debug:
    import logging
    from logging.handlers import TimedRotatingFileHandler

    # https://docs.python.org/3.6/library/logging.handlers.html#timedrotatingfilehandler
    FILE_HANDLER = TimedRotatingFileHandler(
        os.path.join(APP.config["LOG_DIR"], "bamboozler.log"), "midnight"
    )
    FILE_HANDLER.setLevel(logging.WARNING)
    FILE_HANDLER.setFormatter(
        logging.Formatter("<%(asctime)s> <%(levelname)s> %(message)s")
    )
    APP.logger.addHandler(FILE_HANDLER)
