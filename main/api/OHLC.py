from upstox_api.api import *
import datetime
import numpy as np
from requests import exceptions
from api import constants


def get60minStockInfo(scrip):
    close, open, high, low = list(), list(), list(), list()
    scripData = get60minOHLC(scrip)
    for data in scripData:
        close.append(data['close'])
        open.append(data['open'])
        high.append(data['high'])
        low.append(data['low'])
    low = list(map(float, low))
    high = list(map(float, high))
    close = list(map(float, close))
    open = list(map(float, open))
    stock = dict()
    stock['Low'] = np.array(low)
    stock['Close'] = np.array(close)
    stock['High'] = np.array(high)
    stock['Open'] = np.array(open)
    return stock


def get60minOHLC(scrip):
    access_token = constants.access_token
    while True:
        try:
            u = Upstox('JbkKTSUbOp4X6krDd3zCw9yK7XTx5inv2UyE7rKP', access_token)
        except exceptions.HTTPError:
            continue
        break
    u.get_master_contract('NSE_EQ')

    today = datetime.date.today()
    week_ago = today - datetime.timedelta(days=7)

    data2 = extendedData(scrip, u, week_ago, today)
    today = week_ago - datetime.timedelta(days=1)
    week_ago = today - datetime.timedelta(days=7)
    data1 = extendedData(scrip, u, week_ago, today)
    scripData = list()
    for x in data1:
        scripData.append(x)
    for x in data2:
        scripData.append(x)
    return scripData


def extendedData(scrip, u, startDate, endDate):
    while True:
        try:
            scripdata = u.get_ohlc(u.get_instrument_by_symbol('NSE_EQ', scrip), OHLCInterval.Minute_60,
                                   datetime.datetime.strptime(str(startDate), '%Y-%m-%d').date(),
                                   datetime.datetime.strptime(str(endDate), '%Y-%m-%d').date())
        except exceptions.HTTPError:
            print(exceptions.HTTPError.strerror)
            print("exception for: ", scrip)
            continue
        break
    return scripdata