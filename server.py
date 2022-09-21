from flask import Flask, jsonify, render_template, send_file, request,url_for,flash,redirect
from flask_cors import CORS, cross_origin
import tweet as tw
import firebase_admin
import pyrebase
import test
server=Flask(__name__)
cors=CORS(server)
server.config['CORS_HEADERS'] = "Content-Type"
@server.route('/stock',methods=['POST','GET'])
def app():
    data=['Your stock info will be displayed here']
    if request.method=='POST':
      stock=request.form.get('stock')
      data=tw.scrape(stock)
      Data={
        'name':data[0],
        'price':data[1],
        'sentiment':data[2],
        'recommendation':data[3]
      }
      
      test.database.push(Data)
    return render_template('index.html',data=data)
if __name__ ==  '__main__':
  server.run(debug=True)