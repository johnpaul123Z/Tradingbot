import flask
from trade import *
from stockdata import *
from supertrend import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    
    print(supertrend.ATR(10,2,3,3))
    return TEST_APLACA_ROUTE()

app.run()