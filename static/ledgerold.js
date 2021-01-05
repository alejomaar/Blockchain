
class Ledger{
    constructor(){
        this.transactions = [];
    }

    addTransaction(emisor, receptor,cash){
        const transaction = new Transaction(emisor,receptor,cash);
        if(emisor.name==="Sistema"){
            this.transactions.push(transaction);
            return true;
        }
        const balance = this.getBalance(emisor)
        if(this.AvaibleCash(balance,cash)){
            this.transactions.push(transaction);
            return true;
        }else{
            return false;
        }
    }

    AvaibleCash(balance,cost){
        return balance-cost>=0
    }
    getBalance(person){
        var balance =0;
        var personName = person.name;
        this.transactions.forEach(transaction => {
            if(personName===transaction.emisor.name){
                balance -=transaction.cash;
            }if(personName=== transaction.receptor.name){
                balance +=transaction.cash;
            }
        });
        return balance;
    }

    show(listPerson)
    {
        listPerson.forEach((Person) => {
            console.log(Person.name+" :"+this.getBalance(Person));
        });
    }
}


class Transaction {
    constructor(emisor, receptor,cash) {
      this.emisor = emisor;
      this.receptor = receptor;
      this.cash = cash;
    }

    validTransaction(){
        var emisorEqualreceptor = (this.emisor.name===this.receptor.name);
        var isValueEmpty = (this.valor===0);
        //var AvaibleCash = this.emisor.isAvaibleCash(cash);
        //if(this.emisor.name==="Sistema"){AvaibleCash=true}
        if(emisorEqualreceptor || isValueEmpty ){
            return false;
        }else{
            return true;
        }
    }
}

class wallet{
    constructor(name){
        this.name = name;
    }
    getBalance(blockchain){
        var balance =0;
        var name = this.name;
        blockchain.forEach(block => {
            if(name=== block.data.sender){
                balance -=parseInt(block.data.cash);
            }
            if(name===block.data.receiver){
                balance +=parseInt(block.data.cash);
            }
        });
        return balance;
    }
}

class Person{
    constructor(name) {
        this.name = name;
    }
}


function $(id)
{
    return document.getElementById(id);
}

function SendTransaction(){
    var emisorNode =$("emisor");
    var receptorNode =$("receptor");
    var cashNode =$("cash");

    var emisorIndex = parseInt(emisorNode.value);
    var receptorIndex =parseInt( receptorNode.value);
    var cash = parseInt(cashNode.value);

    var emisor = listp[emisorIndex];
    var receptor = listp[receptorIndex];

    var isvalid= ledger.addTransaction(emisor,receptor,cash);
    if(isvalid){
        console.log("Correcto");
        refreshRender();
    }else{
        console.log("Error");
    }
    
    
}

function ShowTransaction(){
    console.log(ledger.show(listp));
}

function refreshRender(){
    var registersNodes = document.querySelectorAll(".register");
    registersNodes.forEach((registerNode,index)=>{
        registerNode.querySelector(".cash").innerHTML= ledger.getBalance(listp[index]);
    });

}