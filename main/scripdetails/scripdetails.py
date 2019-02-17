import pandas_datareader.data as web
import datetime


def getScripDetaile(scrip):
    endTime = datetime.datetime.today()
    startTime = datetime.datetime(2015, 1, 1)
    '''Getting scrip history details from yahoo finance'''
    # print(scrip)
    df = web.DataReader(scrip, "yahoo", startTime, endTime)
    filename = scrip + ".csv"
    df.to_csv(filename)

    return filename