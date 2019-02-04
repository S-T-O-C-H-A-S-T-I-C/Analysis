import pandas_datareader.data as web
import datetime


def getScripDetaile(scrip):
    endTime = datetime.datetime.today()
    startTime = datetime.datetime(2016, 1, 1)

    '''Getting scrip history details from yahoo finance'''
    df = web.DataReader(scrip, "yahoo", startTime, endTime)
    filename = scrip + ".csv"
    df.to_csv(filename)

    return filename