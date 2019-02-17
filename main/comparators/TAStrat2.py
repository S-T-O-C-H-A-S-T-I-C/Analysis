def isItBullish(scrip, ema5, ema8, ema13, rsi, adx, close):
    bullish = True
    emaCross = False
    if ema5[-1] > ema8[-1] and ema8[-1] > ema13[-1]:
        emaCross = True
    bullish = bullish and emaCross
    if adx[-1] < 25:
        bullish = False
    if ema5[-1] > close[-1]:
        bullish = False
    if rsi[-1] < 50:
        bullish = False
    return bullish