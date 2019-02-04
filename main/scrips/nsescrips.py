from stockstats import StockDataFrame
import pandas as pd


def getNSEscrips():
    nifty50 = StockDataFrame.retype(pd.read_csv("ind_nifty50list.csv"))
    nifty500 = StockDataFrame.retype(pd.read_csv("ind_nifty500list.csv"))
    nifty100 = StockDataFrame.retype(pd.read_csv("ind_nifty100list.csv"))
    nifty200 = StockDataFrame.retype(pd.read_csv("ind_nifty200list.csv"))
    niftyauto = StockDataFrame.retype(pd.read_csv("ind_niftyautolist.csv"))
    niftybank = StockDataFrame.retype(pd.read_csv("ind_niftybanklist.csv"))
    niftyfinance = StockDataFrame.retype(pd.read_csv("ind_niftyfinancelist.csv"))
    niftyfmcg = StockDataFrame.retype(pd.read_csv("ind_niftyfmcglist.csv"))
    niftyit = StockDataFrame.retype(pd.read_csv("ind_niftyitlist.csv"))
    niftymedia = StockDataFrame.retype(pd.read_csv("ind_niftymedialist.csv"))
    niftymetal = StockDataFrame.retype(pd.read_csv("ind_niftymetallist.csv"))
    niftynext50 = StockDataFrame.retype(pd.read_csv("ind_niftynext50list.csv"))
    niftypharma = StockDataFrame.retype(pd.read_csv("ind_niftypharmalist.csv"))
    niftyrealty = StockDataFrame.retype(pd.read_csv("ind_niftyrealtylist.csv"))
    stocks = set()

    for stock in nifty50['symbol']:
        stocks.add(stock)

    for stock in nifty500['symbol']:
        stocks.add(stock)

    for stock in nifty100['symbol']:
        stocks.add(stock)

    for stock in nifty200['symbol']:
        stocks.add(stock)

    for stock in niftyauto['symbol']:
        stocks.add(stock)

    for stock in niftybank['symbol']:
        stocks.add(stock)

    for stock in niftyfinance['symbol']:
        stocks.add(stock)

    for stock in niftyfmcg['symbol']:
        stocks.add(stock)

    for stock in niftyit['symbol']:
        stocks.add(stock)

    for stock in niftymedia['symbol']:
        stocks.add(stock)

    for stock in niftymetal['symbol']:
        stocks.add(stock)

    for stock in niftynext50['symbol']:
        stocks.add(stock)

    for stock in niftypharma['symbol']:
        stocks.add(stock)

    for stock in niftyrealty['symbol']:
        stocks.add(stock)

    print("Analysis for", len(stocks), "stocks")
    return list(stocks)

