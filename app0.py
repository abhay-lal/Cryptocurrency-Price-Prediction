#from asyncio.windows_events import NULL
import pandas as pd
import streamlit as st
from tensorflow import keras
import plotly
import plotly.graph_objects as go
import plotly.express

st.title('Bitcoin Price Prediction')
#@st.cache(persist=True)

def week1():
    df = pd.read_pickle('Pickle/week1.pkl')
    fig = go.Figure(data=[go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close_pred'])])
    fig.update_layout(autosize=False,width=850,height=650)
    st.plotly_chart(fig)

def week2():
    df = pd.read_pickle('Pickle/week2.pkl')
    fig = go.Figure(data=[go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close_pred'])])
    fig.update_layout(autosize=False,width=850,height=650)
    st.plotly_chart(fig)

def week3():
    df = pd.read_pickle('Pickle/week3.pkl')
    fig = go.Figure(data=[go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close_pred'])])
    fig.update_layout(autosize=False,width=850,height=650)
    st.plotly_chart(fig)

def week4():
    df = pd.read_pickle('Pickle/week4.pkl')
    fig = go.Figure(data=[go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close_pred'])])
    fig.update_layout(autosize=False,width=850,height=650)
    st.plotly_chart(fig)

def week5():
    df = pd.read_pickle('Pickle/week5.pkl')
    fig = go.Figure(data=[go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close_pred'])])
    fig.update_layout(autosize=False,width=850,height=650)
    st.plotly_chart(fig)   
    
def mapper(forecast_window):
    if forecast_window == '1 Week':
        week1()
    elif forecast_window == '2 Weeks':
        week2()
    elif forecast_window == '3 Weeks':
        week3()
    elif forecast_window == '4 Weeks':
        week4()
    elif forecast_window == '5 Weeks':
        week5()

def graph():
    st.subheader("Latest 200 data points of BTC (Bitcoin)")
    df = pd.read_pickle('Pickle/btc_mini.pkl')
    fig = go.Figure(data=[go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'])])
    fig.update_layout(autosize=False,width=850,height=550)
    st.plotly_chart(fig)
    
def forecasting():
    st.subheader("Select the period (1-5 weeks) into the future for when you would like to see Bitcoin's forecast: ")
    forecast_window = st.selectbox("Choice of Future Forecast Period",options=['1 Week', '2 Weeks', '3 Weeks', '4 Weeks', '5 Weeks'])
    forecast_window_int = mapper(forecast_window)
    
def words():
    st.markdown('In this Deep Learning Application, we have used the price data for Bitcoin to forecast its price in a specified future window.\
    We have used the Tensorflow and Keras APIs to build a stacked LSTM model.')
    
def raw_data():
    st.subheader("You can go through the raw data used for this application using the link below.")
    st.caption('https://www.kaggle.com/c/g-research-crypto-forecasting/data')
    
def main():
    st.image('https://img.etimg.com/thumb/msid-88876988,width-1210,imgsize-53844,,resizemode-4,quality-100/bitcoin-etf.jpg')
    words()
    graph()
    raw_data()
    forecasting()

if __name__ == '__main__':
    main()