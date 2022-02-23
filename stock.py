import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime as dt


#Start of time frame from 4 years ago up until today
start = dt(2018,1,1)
now = dt.now()
#Stock tickers
#If you want to use this project you can add your own stock tickers, just make sure they exist in the time frame
tickers = ["FB", "GS", "NVDA", "MSFT", "TSLA", "AAPL", "CCL", "BA"]
colnames = []

for ticker in tickers:
    data = pdr.get_data_yahoo(ticker, start, now)
    if len(colnames) == 0:
        #Take the closest adjusted price and copy it
        combined = data[['Adj Close']].copy()
    else:
        combined = combined.join(data['Adj Close'])
    #Append to the colnames to know which stock we already added
    colnames.append(ticker)
    combined.columns = colnames
    
print(combined)
        
