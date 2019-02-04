from scripdetails import scripdetails
from stockstats import StockDataFrame
import pandas as pd
import talib
import numpy


if __name__ == '__main__':

    filename = scripdetails.getScripDetaile("hindalco.ns")
    stock = StockDataFrame.retype(pd.read_csv(filename))

    emaclose = talib.EMA(stock['close'], 40)
    print(emaclose)

    adx = talib.ADX(stock['high'], stock['low'], stock['close'], 14)
    print(adx)

    rsi = talib.RSI(stock['close'], 14)
    print(rsi)
