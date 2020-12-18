from flask.json import jsonify, request
from Blockchain import *
from flask import Flask,render_template,jsonify

app =Flask(__name__)
blockchain = Blockchain()

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

@app.route('/show')
def show():
    json = blockchain.JSON()
    return jsonify(json)

    #return render_template('index.html',json)

'''def getchain():
    json = blockchain.JSON()
    return jsonify(json)

def BC():
    blockchain.create(Data("Fernando","51"))
    blockchain.create(Data("rewr","21"))
    blockchain.create(Data("Cris","1000000"))
    '''

if __name__ == '__main__':
    app.run(debug=True)