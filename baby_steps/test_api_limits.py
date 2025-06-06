import requests

for i in range(100):
    requests.get('https://api.binance.com/api/v3/ticker/24hr')
    print(i, end=',', flush=True)
