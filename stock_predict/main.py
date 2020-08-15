#!/usr/bin/env python3
import sys
import os

import data
import plot

def main():
    ticker = sys.argv[1]
    start_date = sys.argv[2]
    end_date = sys.argv[3]
    
    ticker_data = data.get(ticker, start_date, end_date)
    plot.plot_data(ticker_data)
    
if __name__ == "__main__":
    main()