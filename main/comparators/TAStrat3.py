def isItBullish(ema5, ema8, ema13, rsi, adx, close):
    bullish = True
    bullish = bullish and (ema5[-1] > ema8[-1]) and (ema8[-1] > ema13[-1])
    bullish = bullish and (adx[-1] > adx[-3])
    bullish = bullish and (ema5[-1] < close[-1])
    bullish = bullish and (rsi[-1] > 49)
    bullish = bullish and (adx[-1] > 25)
    return bullish