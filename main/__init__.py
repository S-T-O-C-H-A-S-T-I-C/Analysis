from scripdetails import scripdetails
import pandas as pd
from indicators import adx, ema, rsi
from scrips import nsescrips
from comparators import TA


if __name__ == '__main__':

    shortList = list()
    stocks = nsescrips.getNSEscrips()
    for scrip in stocks:
        filename = scripdetails.getScripDetaile(scrip + ".NS")
        stock = pd.read_csv(filename)
        ema_40 = list(ema.getEMA(stock, 40))
        adx_14 = list(adx.getADX(stock, 14))
        rsi_14 = list(rsi.getRSI(stock, 14))
        closingPrice = list(stock['Close'])
        if TA.isItBullish(ema_40[-1], rsi_14[-1], adx_14[-1], closingPrice[-1]):
            shortList.append(scrip)
            print(scrip)
