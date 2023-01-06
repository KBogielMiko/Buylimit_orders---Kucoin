# import neccessary libraries

import sched
import time
import kucoin
import getpass
from datetime import datetime, timedelta
from kucoin.client import Trade

# parameters for Buy Limit transaction

ticker = ''         # string, for example: 'BTC-USDT'
price = '2.1610'    # string, for example: '16056.78'
amount = '0.5'      # string, for example: '0.5'

api_key = getpass.getpass()              # api key of the user
api_secret = getpass.getpass()           # secret key of the user
api_passphrase = getpass.getpass()       # passphrase of the user

# enter to API
client = Trade(key=api_key, secret=api_secret, passphrase=api_passphrase, is_sandbox=False, url='https://api.kucoin.com')

year = 2023
month = 1
day = 5
hour = 19
minute = 8
second = 0

#schedule of transaction

s = sched.scheduler(time.time, time.sleep)
now = datetime.now()
desired_execution_time = time.mktime((year, month, day, hour, minute, second,0,0,0))
s.enterabs(desired_execution_time, 1, client.create_limit_order(ticker, 'buy', amount, price), (s,))

s.run()
