from constants import sizeOfIndicatorsList

def sma40(priceList):
    sma40List = list()
    i = 0
    while i < sizeOfIndicatorsList:
        sum = 0
        cnt = 40
        idx = i
        while cnt > 0:
            cnt -= 1
            sum += priceList[idx]
            idx += 1
        sum /= 40.
        sma40List.append(sum)
        i += 1
    return sma40List