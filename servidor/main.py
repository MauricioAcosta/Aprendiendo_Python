# -*- coding: utf-8 -*-

from flask import Flask;
app = Flask(__name__)

@app.route('/')
def hello_wold():
    return 'Hola, ingenieros :D'

if __name__ == '__main__':
    app.run()
