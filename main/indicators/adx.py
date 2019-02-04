import talib


def getADX(stock, timeLength):
    return talib.ADX(stock['High'], stock['Low'], stock['Close'], timeLength)