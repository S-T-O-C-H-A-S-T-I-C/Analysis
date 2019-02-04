import talib
import numpy as np

def getEMA(stock, timeLength):
    return talib.EMA(stock['Close'], timeLength)