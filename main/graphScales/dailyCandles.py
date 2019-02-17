import scripdetails
import pandas as pd
from indicators import ema, adx, rsi
from comparators import  TAStrat2


def findBullishStocks(stocks):
    shortList = set()
    for scrip in stocks:
        filename = scripdetails.getScripDetaile(scrip + ".NS")
        stock = pd.read_csv(filename)
        ema_13 = list(ema.getEMA(stock, 13))
        ema_5 = list(ema.getEMA(stock, 5))
        ema_8 = list(ema.getEMA(stock, 8))
        adx_14 = list(adx.getADX(stock, 14))
        rsi_14 = list(rsi.getRSI(stock, 14))
        closingPrice = list(stock['Close'])
        if TAStrat2.isItBullish(scrip, ema_5, ema_8, ema_13, rsi_14, adx_14, closingPrice):
            shortList.add(scrip)
    return shortList
