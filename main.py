from flask import Flask
from time import sleep
import random
import logging
import csv
app = Flask(__name__)

logger = logging.getLogger()
logger.setLevel(logging.INFO)


with open('world_cities.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    cities = [row for row in spamreader]


print(len(cities))

@app.route("/")
def hello():
    city = random.choice(cities)
    return f"Hello World!<br>And here is your random city: {city[0]} from {city[2]} in {city[1]}"
