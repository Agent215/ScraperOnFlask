from flask import Flask

app = Flask(__name__)

from testScrape import testScrape
from DarsScrape import DarsScrape
from app import routes