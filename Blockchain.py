from random import *
import hashlib 
import json

class Data:
    def __init__(self,name,cash):
        self.Data = {'Name':name,'Cash':cash}
    #def format(self):
       # return self.Data.Name+"/"+self.Data.Cash
    #return json.dumps(self.Data)

class Blockchain:
    def __init__(self):
        self.blockchain = []#Block Origin
        self.genesis()
    def genesis(self):
        genesis_data = Data("camila","30")
        genesis_block = Block(str(len(self.blockchain)),'0'*64,genesis_data)
        self.blockchain.append(genesis_block)
    def create(self,data):
        block = Block(str(len(self.blockchain)),self.blockchain[-1].Block['hash'],data)
        self.blockchain.append(block)
    def show(self):
        for block in self.blockchain:
            block.show()
    def showhash(self):
        for block in self.blockchain:
            block.showhash()
            
    
class Block:
    def __init__(self,index,prev_hash,Data):
        Hash = self.gethash(index,prev_hash,Data)
        self.Block = {'index':index,'hash':Hash,'prev_hash':prev_hash,'data':Data.Data}

    def gethash(self,index,prev_hash,Data):
        Format= index+'/'+prev_hash+'/'+Data.Data['Name']+'/'+Data.Data['Cash']
        Hash = self.encrypt(Format)
        return Hash
    def encrypt(self,Format):
        return hashlib.sha256(Format.encode()).hexdigest()
    
    def JSON(self):
        return json.dumps(self.Block)
    def show(self):
        Block = self.Block
        print(Block['index'],Block['data'])
    def showhash(self):
        Block = self.Block
        print(Block['index'],Block['hash'],'-',Block['prev_hash'])
    def showall(self):
        print(self.JSON())


blockchain = Blockchain();
blockchain.create(Data("Alejandro","21"))
blockchain.create(Data("Fernando","51"))
blockchain.create(Data("Sofia","21"))
blockchain.showhash()

