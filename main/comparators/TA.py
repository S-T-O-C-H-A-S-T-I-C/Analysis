def isItBullish(ema40, rsi, adx, close):
    bullish = True
    if adx < 25:
        bullish = False
    if ema40 > close:
        bullish = False
    if rsi < 50:
        bullish = False
    return bullish