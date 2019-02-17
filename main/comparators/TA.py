def isItBullish(scrip, ema40, rsi, adx, close):
    if len(ema40) < 5:
        return False
    bullish = True
    if adx[-1] < 30:
        bullish = False
    if ema40[-1] > close[-1]:
        bullish = False
    # if rsi[-1] < 50:
    #     bullish = False
    # if ema40[-2] < close[-2]:
    #     bullish = False
    return bullish