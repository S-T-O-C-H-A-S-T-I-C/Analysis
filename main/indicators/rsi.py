import talib


def getRSI(stock, timeLength):
    return talib.RSI(stock['Close'], timeLength)