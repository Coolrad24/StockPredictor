import requests
url='https://mattbaifinanceproject.sunyu912.repl.co/stockInfo/'
stock=input('give me stock')
req=requests.get(url+stock)
print(req.json())