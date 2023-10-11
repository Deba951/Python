"""As machine learning practitioners, we need to collect stock price data for regression analysis and time series analysis. 
We can easily download it from Yahoo Finance. 
But if we want to create an application where we can analyze the real-time stock prices, we need to collect the latest dataset instead of using the downloaded dataset.

Yahoo Finance is one of the most popular websites to collect stock price data. 
We need to visit the website, enter the company’s name or stock symbol, and you can easily download the dataset. 
But to get the latest dataset every time running the code, we need the yfinance API. 
yfinance is an API provided by Yahoo Finance to collect the latest stock price data.

To use this API, firstly install it by using the pip or pip3 command in the terminal or command prompt as mentioned below:
pip3 install yfinance
"""

import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
today = date.today()

d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=360)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2

data = yf.download('AAPL', 
                      start=start_date, 
                      end=end_date, 
                      progress=False)

print(data.head())

"""
The above code will collect the stock price data from today to the last 360 days. In this dataset, Date is not a column, it’s the index of this dataset. 
To use this data for any data science task, we need to convert this index into a column. Below is the process:
"""

data["Date"] = data.index
data = data[["Date", "Open", "High", 
             "Low", "Close", "Adj Close", "Volume"]]

data.reset_index(drop=True, inplace=True)

print(data.head())