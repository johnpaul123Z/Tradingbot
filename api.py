import flask
from trade import *
from stockdata import *


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    
    return TEST_APLACA_ROUTE()

app.run()