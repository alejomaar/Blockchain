from random import *
import hashlib
import json

class Data:
    def __init__(self,name,cash):
        self.Data = {'Name':name,'Cash':cash}
    def JSON(self):
        return json.dumps(self.Data)

class Blockchain:
    def __init__(self):
        self.blocks = []#Block Origin
        dataOrigin = Data("Camila",30)
        blockOrigin = Block(0,self.gethash(dataOrigin),0,dataOrigin)
        self.blocks.append(blockOrigin)
    def gethash(self,data):
        return hashlib.md5(data.JSON().encode()).hexdigest()
        #return randint(1, 100)
    def create(self,data):
        block = Block(len(self.blocks),self.gethash(data),self.prevhash(),data)
        self.blocks.append(block)
    def prevhash(self):
        return self.blocks[-1].H

    def show(self):
        for block in self.blocks:
            print(block.data.JSON())
            print("I:",block.index,"#",block.H,"<-#",block.prev_hash)

    
class Block:
    def __init__(self,index,H,prev_hash,data):
        self.index = index
        self.H = H
        self.prev_hash = prev_hash
        self.data = data


    
blockchain = Blockchain();
blockchain.create(Data("Alejandro",21));
blockchain.create(Data("Fernando",51));
blockchain.create(Data("Sofia",70));
blockchain.show();
