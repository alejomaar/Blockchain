from Blockchain import *
from flask import Flask,render_template,jsonify,request
from flask_socketio import SocketIO,send
import json

app =Flask(__name__)
app.config['SECRET_KEY']='secret'
socketio = SocketIO(app)

blockchain = Blockchain()

@socketio.on('message')
def handleMessage(msg):
    global blockchain
    #Data = json.loads(msg)
    Block = blockchain.create(Data(msg["Name"],msg["Cash"]))    
    send(json.dumps(Block), broadcast=True)

@app.route('/')
def home():
    return render_template('index.html')

'''@app.route('/add',methods=['POST'])
def add():
    global blockchain
    if request.method == "POST":
        req = request.form

        name = req["Name"]
        cash = req["Cash"]

        blockchain.create(Data(name,cash))

        json = blockchain.JSON()
        return jsonify(json)
    else:
        return "Invalid",404'''


if __name__ == '__main__':
    socketio.run(app)
    #app.run(debug=True)