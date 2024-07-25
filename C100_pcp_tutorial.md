Debug the Code
======================
In this activity, you will learn to connect to sepolia and remove the sender for an admin panel.
<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10759141/C100PCP.gif" width = "100%" height = "50%">


Follow the given steps to complete this activity.


1. Admin panel
* Get the senders address from the account.
```
sender =accountAddress
```

* Connect to Sepolia url using the variable `sepoliaUrl`.
```
sepoliaUrl = "https://sepolia.infura.io/v3/7cc0d838c6304750ab8f26877179b0b3" 
web3 = Web3(Web3.HTTPProvider(sepoliaUrl))
```
Note: Comment the Ganache server connection code.
```
#ganacheUrl = "http://127.0.0.1:7545" 
#web3 = Web3(Web3.HTTPProvider(ganacheUrl))
```


* Save and run the code to check the output.
