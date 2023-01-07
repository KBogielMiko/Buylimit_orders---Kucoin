import getpass
import kucoin
import sched
import time
from datetime import datetime, timedelta
from kucoin.client import Trade

# parameters for Buy Limit transaction

ticker = 'PIAS-USDT'         # string - pair we are interested in, for example: 'BTC-USDT'
price = '0.0679'          # string - price we are interested to create Buy Limit order,for example: '16056.78'
amount = '20'         # string - amount we are interested to buy, for example: '0.5' (half of the coin)

api_key = ''                             # api key of the user
api_secret = ''                          # secret key of the user
print("Please enter your password")
api_passphrase = getpass.getpass()       # passphrase of the user
print(api_passphrase)
# enter to API
client = Trade(key=api_key, secret=api_secret, passphrase=api_passphrase, is_sandbox=False, url='https://api.kucoin.com')

#schedule of transaction
date = '2023-01-07 15:39:00.000'           # string - date we are interested to create Buy Limit order, for example: '2023-01-06 20:03:00.043' (date has to be given in exact format)

s = sched.scheduler(time.time, time.sleep)

def run_command():
    order = client.create_limit_order(ticker, 'buy', amount, price)
    return order

run_time = time.mktime(time.strptime(date, '%Y-%m-%d %H:%M:%S.%f'))
s.enterabs(run_time, 1, run_command(), (s,))

s.run()
