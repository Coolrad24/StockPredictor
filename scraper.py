import tweet as tw
import test
import requests
from bs4 import BeautifulSoup
test.database.remove()
def getData(stock):
    data=tw.scrape(stock)
    Data={  
    'name':data[0],
    'price':data[1],
    'sentiment':data[2],
    'recommendation':data[3]
    }

    test.database.child(stock).set(Data)
req=requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup=BeautifulSoup(req.content,'html.parser')
tickers=soup.find_all('a',class_='external text')
for t in tickers:
    try:
        getData(t.get_text())
        print(t.get_text()+'has been uploaded')
    except:
        pass


