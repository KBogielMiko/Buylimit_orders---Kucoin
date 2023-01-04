pip install kucoin-python
from kucoin.client import Trade
def buy_order(ticker, price, amount, api_key, api_secret, api_passphrase):
    client = Trade(key=api_key, secret=api_secret, passphrase=api_passphrase, is_sandbox=False, url='https://api.kucoin.com')
    order_id = client.create_limit_order(ticker, 'buy', amount, price)
    return order_id
buy_order(ticker = '', price = '', amount = '' , api_key = '', api_secret = '', api_passphrase='')
