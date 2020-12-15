import hashlib 
#import json
#import time

class Data:
    def __init__(self,name,cash):
        self.Data = {'Name':name,'Cash':cash}

class Blockchain:
    def __init__(self):
        self.blockchain = []#Block Origin
        self.genesis()
    def genesis(self):
        genesis_data = Data("","0")
        genesis_block = Blockchain.Block(str(len(self.blockchain)),'0'*64,genesis_data)
        self.blockchain.append(genesis_block)
    def create(self,data):
        block = Blockchain.Block(str(len(self.blockchain)),self.blockchain[-1].Block['hash'],data)
        self.blockchain.append(block)
    def JSON(self):
        json = [];
        for block in self.blockchain:
            json.append(block.JSON())
        return json
    def show(self):
        print("\n\n")
        for block in self.blockchain:      
            block.show()
    def showhash(self):
        print("\n\n")
        for block in self.blockchain:
            block.showhash()


    class Block:
        def __init__(self,index,prev_hash,Data):
            Hash,nonce = self.proof_of_work(index,prev_hash,Data)
            self.Block = {'index':index,'nonce':nonce,'hash':Hash,'prev_hash':prev_hash,'data':Data.Data}

        def proof_of_work(self,index,prev_hash,Data):
            Info= index+'/'+prev_hash+'/'+Data.Data['Name']+'/'+Data.Data['Cash']
            hash=''
            nonce=0
            
            while(not self.is_hash_valid(hash)):
                temp = Info+str(nonce)
                hash = hashlib.sha256(temp.encode()).hexdigest()
                nonce+=1

            return hash,nonce
        def is_hash_valid(self,hash):
            return (hash.startswith('0'*3))
        #def encrypt(self,Format):
            #return 
        
        def JSON(self):
            return self.Block
            #return {'index':self.Block['index'],'data':self.Block['data']}
            #return json.dumps(self.Block)
        def show(self):
            Block = self.Block
            print(Block['index'],Block['data'])
        def showhash(self):
            Block = self.Block
            print(Block['index'],Block['hash'],'-',Block['prev_hash'])
             
    
'''start_time = time.time()
blockchain = Blockchain();
blockchain.create(Data("alejandro","20"))
blockchain.create(Data("Fernando","51"))
blockchain.create(Data("Sofia","21"))
blockchain.show()
blockchain.showhash()
print("--- %s seconds ---" % (time.time() - start_time))'''

