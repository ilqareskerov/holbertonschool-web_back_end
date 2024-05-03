#!/usr/bin/env python3
''' module to learn i18n
'''
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config():
    ''' Configuration class
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    ''' returns index.html file
    '''
    return render_template('0-index.html')


@babel.localeselector
def get_locale():
    ''' using get_locale function
    '''
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
