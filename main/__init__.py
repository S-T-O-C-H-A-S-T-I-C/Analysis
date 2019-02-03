from scripdetails import scripdetails
from indicators import sma40, ema40
if __name__ == '__main__':
    closingPriceDF, filename = scripdetails.getScripDetaile("hindalco.ns")
    closingPriceDF = reversed(closingPriceDF)
    priceList = [price for price in closingPriceDF]
    sma40List = sma40.sma40(priceList)
    print(sma40List[:10])

    ema40List = ema40.ema40(priceList, sma40List)
    print(ema40List[:10])