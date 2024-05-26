import flask
from trade import *
from stockdata import *


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    bardata('spy','1Day')
    return TEST_APLACA_ROUTE()

app.run()