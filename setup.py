from Blockchain import *
from flask import Flask,render_template,jsonify,request
from flask_socketio import SocketIO,send
import json

app =Flask(__name__)
#app.config['SECRET_KEY']='secret'
socketio = SocketIO(app)

blockchain = Blockchain()

@socketio.on('message')
def handleMessage(msg):
    global blockchain
    #Data = json.loads(msg)
    Block = blockchain.create(Data(msg["sender"],msg["receiver"],msg["cash"]))    
    send(json.dumps(Block), broadcast=True)

@app.route('/getBlockchain')
def getBlockchain():
    return jsonify(blockchain.JSON());

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ledger')
def ledger():
    return render_template('ledger.html')


if __name__ == '__main__':
    socketio.run(app)
    #socketio.run(app,debug=True)
    #app.run(debug=True)