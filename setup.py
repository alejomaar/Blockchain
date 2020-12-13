from flask.json import jsonify
from Blockchain import *
from flask import Flask,render_template,jsonify

app =Flask(__name__)

@app.route('/')
def home():
    json = BC()
    return jsonify(json)
    #return render_template('index.html',json)

def BC():
    blockchain = Blockchain()
    blockchain.create(Data("alejandro","20"))
    blockchain.create(Data("Fernando","51"))
    blockchain.create(Data("Sofia","21"))
    json = blockchain.JSON()
    return json
if __name__ == '__main__':
    app.run(debug=True)