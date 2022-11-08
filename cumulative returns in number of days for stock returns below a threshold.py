import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt 
import numpy as np
import datetime
from datetime import date
from datetime import timedelta

# creating function for 3 inputs
def myfunc(ticker, Return, Days):
    
    # Getting data for 1 YEAR   
    df = yf.Ticker(ticker).history(interval='1d', period='1y').Close.pct_change() 
    df=df.to_frame('returns') 
    df['cum_returns'] = (df['returns'] + 1).cumprod() - 1
    
    #setting a return threshold 
    #getting cumulative returns in number of days for stock returns below that threshold
    
    for i in range(len(df)):       
        if df.returns.iloc[i] < Return: 
            i = i + 1
            df2 = df.cum_returns.iloc[i:i+Days].to_list()
            plt.plot(df2)
            plt.xlabel("Date")
            plt.ylabel("Growth of $1 investment")
            plt.title("Daily cumulative returns data")
    return(plt.show())
            
#Test function
myfunc('AMZN', -0.025, 10)


    
