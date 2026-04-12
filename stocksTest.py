import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

ticker = st.text_input("Ticker", "AAPL")
days = st.slider("Days back", 5, 60, 30)

end = datetime.today()
start = end - timedelta(days=days)

data = yf.download(ticker, start=start, end=end)

price = data["Close"]
st.write("Sparkline:")
st.bar_chart(price)

st.write("Price data:")
st.dataframe(price)


