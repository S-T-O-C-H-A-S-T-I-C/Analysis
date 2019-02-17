import talib


def getEMA(stock, timeLength):
    return talib.EMA(stock['Close'], timeLength)