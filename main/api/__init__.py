from upstox_api.api import *
import datetime
from api import constants

if __name__ == '__main__':
    '''
s = Session('JbkKTSUbOp4X6krDd3zCw9yK7XTx5inv2UyE7rKP')
s.set_redirect_uri('http://127.0.0.199')
s.set_api_secret('86mrhcnf2b')
print(s.get_login_url())

    Login to the above url and copy code in next line call
s.set_code('5438fff8f2455b29d2f9c8c5cbfb7c300f5a404c')
access_token = s.retrieve_access_token()
print('Received access_token: %s' % access_token)
    '''

    '''Creating upstox object with api key as first arg'''
    access_token = constants.access_token
    print(access_token)
    print(access_token)
    u = Upstox('JbkKTSUbOp4X6krDd3zCw9yK7XTx5inv2UyE7rKP', access_token)
    nseeq = u.get_master_contract('NSE_EQ')
    print('printing nse eq')
    print(nseeq)
    tatasteel_nse_eq = u.get_instrument_by_symbol('NSE_EQ', 'TATASTEEL')

    today = datetime.date.today()
    week_ago = today - datetime.timedelta(days=7)
    scrip = 'TATASTEEL'

    print("scrip: ", scrip)
    data2 = scripdata = u.get_ohlc(u.get_instrument_by_symbol('NSE_EQ', scrip), OHLCInterval.Day_1,
                                   datetime.datetime.strptime(str(week_ago), '%Y-%m-%d').date(),
                                   datetime.datetime.strptime(str(today), '%Y-%m-%d').date())
    today = week_ago - datetime.timedelta(days=1)
    week_ago = today - datetime.timedelta(days=7)
    data1 = u.get_ohlc(u.get_instrument_by_symbol('NSE_EQ', scrip), OHLCInterval.Day_1,
                                   datetime.datetime.strptime(str(week_ago), '%Y-%m-%d').date(),
                                   datetime.datetime.strptime(str(today), '%Y-%m-%d').date())
    scripData = list()
    for x in data1:
        scripData.append(x)
    for x in data2:
        scripData.append(x)

    for x in scripData:
        print(x)
    print(scripData)


