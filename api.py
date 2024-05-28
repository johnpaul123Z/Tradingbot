import flask
from trade import *
from stockdata import *
from supertrend import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    st = supertrend()
    # Call the Truerange method on the instance
    result = st.Truerange()
    print("Truerange:", result)
    return TEST_APLACA_ROUTE()

app.run()