import tweepy
import config
import string as st
from textblob import TextBlob as tb
import yfinance as yf
def scrape(ticker):
  data=[]
  
  ticker = yf.Ticker(ticker)
  price=ticker.info['regularMarketPrice']
  coName = ticker.info['longName']
  data.append(coName)
  data.append(price)
  
  
  client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
  response = client.search_recent_tweets(query=coName, max_results=100)
  tweets = []
  def splitTwo(string):
    arr=[]
    for s in string:
      arr.append(s)
    return arr
  
  
  for r in response.data:
      string = str(r.text)
      string = string.split(' ')
      tweets.append(string)
  for t in tweets:
    
    dIndex=[]
    for i in range(len(t)):
        chars=splitTwo(t[i])
        
        if (t[i] == 'RT'):
            t[i]=''
        elif ('@' in t[i] and len(t[i]) > 1):
            t[i]=''
        elif ('#' in t[i]):
            t[i]=''
        elif ('https' in t[i]):
            t[i]=''
        else: 
          for char in chars:
            if(char in st.punctuation or char=="…" or char=="‘" or char=='“' or char=="’"):
              del chars[chars.index(char)]
          t[i]="".join(chars)
    
  g=0
  b=0
  n=0
  realTweets=[]
  for t in tweets:
    realTweets.append(" ".join(t))
  for r in realTweets:
    s=tb(r)
    if(s.polarity>0):
      g+=1
    elif(s.polarity<0):
      b+=1
    else:
      n+=1
  sentiment=""
  recommend=''
  if(g>b):
    sentiment=('sentiment is good')
  else:
    sentiment=('sentiment is bad')
  if(g>b):
    if(n>(len(realTweets)/2)):
      recommend=('we recommend you wait')
    else:
      recommend=('we recommend you buy/hold')
  else:
    if(n>(len(realTweets)/2)):
      recommend=('we recommend you wait')
    else:
      recommend=('we recommend you sell/dont buy')
  data.append(sentiment)
  data.append(recommend)
  return data
  
  
'''
import string as st
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
roberta='cardiffnlp/twitter-roberta-base-sentiment'
model=AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer=AutoTokenizer.from_pretrained(roberta)
tweet=input('give me tweet')
labels=['Negative',"Nuetral",'Positive']
analysis=tokenizer(tweet,return_tensors='pt')
print(analysis)
sentiment=model(**analysis)
sentiment=sentiment[0][0].detach().numpy()
print(sentiment)
good=sentiment[0]
neut=sentiment[1]
bad=sentiment[2]
most=0
mostIndex=0
Sentiment=[]
for s in sentiment:
  Sentiment.append(s)
for s in Sentiment:
  if abs(s)>most:
    most=abs(s)
    mostIndex=Sentiment.index(s)
print("your tweet's sentiment is "+labels[mostIndex])
'''


