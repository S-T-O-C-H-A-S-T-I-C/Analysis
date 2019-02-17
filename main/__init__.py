from scrips import nsescrips
from graphScales import dailyCandles, hourCandles


if __name__ == '__main__':

    shortList = list()
    stocks = nsescrips.getNSEscrips()
    # for scrip in stocks:
    #     filename = scripdetails.getScripDetaile(scrip + ".NS")
    #     stock = pd.read_csv(filename)
    #     ema_13 = list(ema.getEMA(stock, 13))
    #     ema_5 = list(ema.getEMA(stock, 5))
    #     ema_8 = list(ema.getEMA(stock, 8))
    #     adx_14 = list(adx.getADX(stock, 14))
    #     rsi_14 = list(rsi.getRSI(stock, 14))
    #     closingPrice = list(stock['Close'])
    #     if TAStrat2.isItBullish(scrip, ema_5, ema_8, ema_13, rsi_14, adx_14, closingPrice):
    #         shortList.append(scrip)
    #         print("BUY", scrip)
    # dailyCandleBullish = dailyCandles.findBullishStocks(stocks)
    # print("Bullish stocks on basis of daily candles: ")
    # for stock in dailyCandleBullish:
    #     print(stock)

    hourCandlesBullish = hourCandles.findBullishStocks(stocks)
    print("\nBullish stocks on basis of hourly candles: ")
    for stock in hourCandlesBullish:
        print(stock)
