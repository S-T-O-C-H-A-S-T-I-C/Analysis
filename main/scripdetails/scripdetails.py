import pandas_datareader.data as web
import datetime
import logging

def getScripDetaile(scrip):
    logging.log(0, "Getting scrip details: " + scrip)

    endTime = datetime.datetime.today()
    startTime = datetime.datetime(2017, 1, 1)

    '''Getting scrip history details from yahoo finance'''
    df = web.DataReader(scrip, "yahoo", startTime, endTime)
    filename = scrip + ".csv"
    df.to_csv(filename)
    closingPrice = df.iloc[1:, -1]

    '''print(closingPrice)'''
    return closingPrice, filename