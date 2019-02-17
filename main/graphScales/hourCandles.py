from indicators import ema, adx, rsi
from comparators import TAStrat2, TAStrat3
from api import OHLC


def findBullishStocks(stocks):
    shortList = set()
    stocks = set(stocks)
    stocks.remove('UNITECH')
    for stock in stocks:
        print(stock)
        stockINFO = OHLC.get60minStockInfo(stock)
        ema_13 = list(ema.getEMA(stockINFO, 13))
        ema_5 = list(ema.getEMA(stockINFO, 5))
        ema_8 = list(ema.getEMA(stockINFO, 8))
        adx_14 = list(adx.getADX(stockINFO, 14))
        rsi_14 = list(rsi.getRSI(stockINFO, 14))
        closingPrice = stockINFO['Close']
        if TAStrat2.isItBullish(stock, ema_5, ema_8, ema_13, rsi_14, adx_14, closingPrice):
            shortList.add(stock)
            print("BUY", stock)

    return shortList