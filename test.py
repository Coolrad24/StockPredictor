import firebase_admin
import pyrebase
config={
  'apiKey': "AIzaSyBe1k6nqnIFKAdBqKvmJ2wGALSW4FdyhTA",
  'authDomain': "stockpredictor-5d47b.firebaseapp.com",
  'projectId': "stockpredictor-5d47b",
  'databaseURL':'https://stockpredictor-5d47b-default-rtdb.firebaseio.com/',
  'storageBucket': "stockpredictor-5d47b.appspot.com",
  'messagingSenderId': "476741430849",
  'appId': "1:476741430849:web:b7dbc0f69101216d84e0c0",
  'measurementId': "G-G87RY7RKTF"
}
firebase=pyrebase.initialize_app(config)
database=firebase.database()
data=['Nintendo Co., Ltd.', 56, 'sentiment is bad', 'we recommend you sell/dont buy']
Data={
    'name':data[0],
    'price':data[1],
    'sentiment':data[2],
    'recommendation':data[3]
}
