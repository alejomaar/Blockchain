from Blockchain import *
from flask import Flask,render_template,jsonify,request
from flask_socketio import SocketIO,send

app =Flask(__name__)
app.config['SECRET_KEY']='secret'
socketio = SocketIO(app)

blockchain = Blockchain()

@socketio.on('message')
def handleMessage(msg):
    print("mesage",msg)
    send(msg, broadcast=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add',methods=['POST'])
def add():
    global blockchain
    if request.method == "POST":
        req = request.form

        name = req["Name"]
        cash = req["Cash"]

        blockchain.create(Data(name,cash))

        json = blockchain.JSON()
        #return jsonify({"m1":"data1","m2":"data2"})
        return jsonify(json)
        #return "success",201
    else:
        return "Invalid",404

#@app.route('/show')
#def show():
    #json = blockchain.JSON()
    
    #return jsonify(json)

    #return render_template('index.html',json)



if __name__ == '__main__':
    socketio.run(app)
    #app.run(debug=True)