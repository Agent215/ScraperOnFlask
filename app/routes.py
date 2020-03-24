from app import app
from flask import jsonify

from testScrape import testScrape
from DarsScrape import DarsScrape
# get the request module and name it as uReq for future use


@app.route('/')
@app.route('/index')
def index():
    return  jsonify(courses=DarsScrape())


