import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math
import alpaca_trade_api as tradeapi

from secrets import *

'''
# Read CSV file that has a list of the S&P 500 company names
stocks = pd.read_csv('sp_500_stocks.csv')

# API Calls

# Get market capitalization for each stock
symbol = 'AAPL'
api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote/?token={IEX_CLOUD_API_TOKEN}'
# API Call and save as JSON
data = requests.get(api_url).json()
print(data)
'''

# api_url = 'https://paper-api.alpaca.markets/v2/account'

api = tradeapi.REST(
    APCA_API_KEY_ID,
    APCA_SECRET_KEY,
    APCA_DOMIAN
)

account = api.get_account()

# Check if our account is restricted from trading.
if account.trading_blocked:
    print('Account is currently restricted from trading.')

# Check how much money we can use to open new positions.
print('${} is available as buying power.'.format(account.buying_power))


balance_change = float(account.equity) - float(account.last_equity)
print(f'Today\'s portfolio balance change: ${balance_change}')

symbol = 'IBM'
url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}'


url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}'
data = requests.get(url).json()

print(data['MarketCapitalization'])



