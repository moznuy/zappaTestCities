import csv
import logging
import random

from flask import Flask, render_template

app = Flask(__name__, static_url_path='')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


with open('world_cities.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    cities = [row for row in spamreader]


@app.route("/")
def hello():
    city_row = random.choice(cities)
    return render_template('index.html', city=city_row[0], province=city_row[2], country=city_row[1])


@app.route('/favicon.svg')
def root():
    return app.send_static_file('favicon.svg')

