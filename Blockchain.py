from random import *

class Data:
    def __init__(self,name):
        self.name = name

class Blockchain:
    def __init__(self):
        self.blocks = []#Block Origin
        blockOrigin = Block(0,self.gethash(),0,Data("Camila"))
        self.blocks.append(blockOrigin)
    def gethash(self):
        return randint(1, 100)
    def create(self,data):
        block = Block(len(self.blocks),self.gethash(),self.prevhash(),data)
        self.blocks.append(block)
    def prevhash(self):
        return self.blocks[-1].H

    def show(self):
        for block in self.blocks:
            print("I:",block.index,"#",block.H,"<-#",block.prev_hash,"Name",block.data.name)

    
class Block:
    def __init__(self,index,H,prev_hash,data):
        self.index = index
        self.H = H
        self.prev_hash = prev_hash
        self.data = data


    
blockchain = Blockchain();
blockchain.create(Data("Alejandro"));
blockchain.create(Data("Fernando"));
blockchain.create(Data("Sofia"));
blockchain.show();
