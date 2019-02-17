import os


def createSwingTradeList(stocks):
    file = open("SwingTrading.txt", "w")
    for stock in stocks:
        file.write(stock)
    os.system("notepad SwingTrading.txt")
