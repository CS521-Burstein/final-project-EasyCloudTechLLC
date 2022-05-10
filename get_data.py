# Source: https://pypi.org/project/yfinance/

import pandas as pd
import yfinance as yf
import os

def get_stock(ticker, start_date, end_date):
    try:
        yf.pdr_override()
        df = yf.download(ticker, start=start_date, end=end_date)
        # read stock date as index
        df['Date'] = df.index
        df['Date'] = pd.to_datetime(df['Date'])
        # Separate date, easy to the data analysis
        df['Year'] = df['Date'].dt.year
        df['Month'] = df['Date'].dt.month
        df['Day'] = df['Date'].dt.day
        # tag
        for tag in ['Open', 'High', 'Low']:
            df[tag] = df[tag].round(2)
        tag_list = ['Year', 'Month', 'Day', 'Open',
                    'High', 'Low', 'Close', 'Volume', 'Adj Close']
        df = df[tag_list]
        return df
    except Exception as error:
        print(error)
        return None


# def current_path():
#    print("Current working directory before")
#    print(os.getcwd())
#    print()
# current_path()
# os.chdir('../')
# current_path()

try:
    ticker = "SPY"
    curPath = os.getcwd()
    outputPath = os.path.join(curPath, ticker + '.csv')
    #  Sep, 2001, '9/11'
    #  Mar,  2003, 'Iraq War'
    df = get_stock(ticker, start_date='2001-08-01', end_date='2004-03-31')
    df.to_csv(outputPath, index=False)
except Exception as error:
    print('Download stock ' + ticker + ' error')






