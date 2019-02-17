import os


def createSwingTradeList(stocks):
    file = open("SwingTradingLongInitiated.txt", "w")
    for stock in stocks:
        file.write(stock)
    os.system("notepad SwingTradingLongInitiated.txt")
