from constants import sizeOfIndicatorsList
def ema40(priceList, sma40List):
    ema40List = sma40List
    idx = sizeOfIndicatorsList - 1
    idx -= 1
    while idx >=0:
        ema40List[idx] = priceList[idx]*(2./41) + ema40List[idx+1]*(1-(2./41))
        idx -= 1
    return ema40List
    return 0