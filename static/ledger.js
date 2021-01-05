class ledger{
    static getLedger(blockchain){
        var names=[];
        var balance=[];
        blockchain.shift();
        blockchain.forEach(block => {
            let senderIndex = names.indexOf(block.data.sender);
            if(senderIndex==-1 ){
                names.push(block.data.sender);
                balance.push(-parseInt(block.data.cash));
            }else{
                balance[senderIndex]-=parseInt(block.data.cash);
            }
            let receiverIndex = names.indexOf(block.data.receiver);
           
            if(receiverIndex==-1 ){
                names.push(block.data.receiver);
                balance.push(parseInt(block.data.cash));
            }else{
                balance[receiverIndex]+=parseInt(block.data.cash);
            }
        });
        return {names,balance};
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


function $(id)
{
    return document.getElementById(id);
}

function refreshRender(blockchain){
    var {names,balance}= ledger.getLedger(blockchain);
    var ledgerNode = document.querySelector(".ledger");
    ledgerNode.innerHTML="";
    var accountNode = document.querySelector(".register");
    names.forEach((name,index)=>{
        var cloneAccount = accountNode.cloneNode(true);
        cloneAccount.style.display = "block";
        cloneAccount.querySelector(".name").innerHTML= name;
        cloneAccount.querySelector(".cash").innerHTML= balance[index];
        ledgerNode.appendChild(cloneAccount);
    });
}