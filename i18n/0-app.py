#!/usr/bin/env python3
''' module to learn i18n
'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    ''' returns index.html file
    '''
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
