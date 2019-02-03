import pandas_datareader.data as web
import datetime
import logging


def getScripDetaile(scrip):
    logging.log(0, "Getting scrip details: " + scrip)

    endTime = datetime.datetime.today()
    startTime = datetime.datetime(2018, 8, 1)
    df = web.DataReader(scrip, "yahoo", startTime, endTime)
    filename = scrip + ".csv"
    df.to_csv(filename)
    return filename