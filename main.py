import getpass
import kucoin
import sched
import time
from datetime import datetime, timedelta
from kucoin.client import Trade

# parameters for Buy Limit transaction

ticker = ''         # string - pair we are interested in, for example: 'BTC-USDT'
price = ''          # string - price we are interested to create Buy Limit order,for example: '16056.78'
amount = ''         # string - amount we are interested to buy, for example: '0.5' (half of the coin)

api_key = ''                             # api key of the user
api_secret = ''                          # secret key of the user
print("Please enter your password")
api_passphrase = getpass.getpass()       # passphrase of the user
print(api_passphrase)
quit()

# enter to API
client = Trade(key=api_key, secret=api_secret, passphrase=api_passphrase, is_sandbox=False, url='https://api.kucoin.com')

#schedule of transaction
date = ''           # string - date we are interested to create Buy Limit order, for example: '2023-01-06 20:03:00.043' (date has to be given in exact format)

s = sched.scheduler(time.time, time.sleep)
now = datetime.now()
desired_execution_time = time.mktime((int(data[:4]), int(data[5:7]), int(data[8:10]), int(data[11:13]), int(data[14:16]), int(data[17:19]),int(data[20]),int(data[21]),int(data[22])))
s.enterabs(desired_execution_time, 1, client.create_limit_order(ticker, 'buy', amount, price), (s,))

s.run()
