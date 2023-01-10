import getpass
import sched
import time as time_module

from datetime import datetime, timedelta
from kucoin.client import Trade

# Parameters for Buy Limit transaction
ticker = ''             # string - pair we are interested in, for example: 'BTC-USDT'
price = ''              # string - price we are interested to create Buy Limit order,for example: '16056.78'
amount = ''             # string - amount we are interested to buy, for example: '0.5' (half of the coin)
date = ''               # string - date we are interested to create Buy Limit order, for example: '2023-01-06 20:03:00' (date has to be given in exact format)


# Parameters for API initialization
api_key = ''                                                    # api key of the user
api_secret = ''                                                 # secret key of the user
print("Please enter your passphrase")
api_passphrase = getpass.getpass()                              # passphrase of the user


# Client initialization
client = Trade(key=api_key, secret=api_secret, passphrase=api_passphrase, is_sandbox=False, url='https://api.kucoin.com')


# Schedule of transaction
def run_command(): client.create_limit_order(ticker, 'buy', amount, price)

scheduler = sched.scheduler(time_module.time, time_module.sleep)

t = time_module.strptime(date, '%Y-%m-%d %H:%M:%S')
t = time_module.mktime(t)

scheduler_e = scheduler.enterabs(t, 1, run_command, ())

scheduler.run()
