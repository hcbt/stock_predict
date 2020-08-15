from pandas_datareader import data as pdr

import yfinance as yf

yf.pdr_override()

def get(ticker, start_date, end_date):    
    data = pdr.get_data_yahoo(ticker, start = start_date, end = end_date)
    data.reset_index(inplace = True)
    return data