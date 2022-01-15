import pandas as pd
from flask import Flask, request, render_template
from flasgger import Swagger
from tensorflow import keras
import json
import plotly
import plotly.graph_objects as go
import plotly.express

app = Flask(__name__,template_folder='D:\Projects\\New folder\g-research-crypto-forecasting')
Swagger(app)

model = keras.models.load_model("btc.h5")

@app.route('/')
def welcome():
    return "Welcome!"
@app.route('/graph')
def graph():
    df = pd.read_pickle('btc_mini.pkl')
    fig = go.Figure(data=[go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'])])
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('btc_mini.html', graphJSON=graphJSON)
@app.route('/predict')
def pred():

    x = 1
    return x

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)