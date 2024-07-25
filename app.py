from flask import Flask, render_template, request, redirect
import os
from time import time
from wallet import Account, Wallet
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def firebaseInitialization():
    cred = credentials.Certificate("config/serviceAccountKey.json")
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://blockchain-wallet-a2812-default-rtdb.firebaseio.com'})
    print("🔥🔥🔥🔥🔥 Firebase Connected! 🔥🔥🔥🔥🔥")

firebaseInitialization()

STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)
app.use_static_for_root = True

ref = db.reference('adminAccount/')
account= ref.get()
if(not account):
    account = Account()

myWallet =  Wallet()


@app.route("/", methods= ["GET", "POST"])
def index():
    global account, myWallet
      
    isConnected = myWallet.checkConnection()
    balance = "No Balance"
    if(account):
        if(type(account)==dict):
            balance = myWallet.getBalance(account['address'])
        else:
            balance = myWallet.getBalance(account.address)

    return render_template('index.html', isConnected=isConnected,  account= account, balance = balance)

   
@app.route('/transactions')
def transactions():
    global account, myWallet    
    transactions = None
    if(type(account)==dict):
         transactions = myWallet.getTransactions(account['address'])
    else:
         transactions = myWallet.getTransactions(account.address)

    return render_template('transactions.html', account=account, transactions= transactions)

@app.route("/makeTransaction", methods = ["GET", "POST"])
def makeTransaction():
    global myWallet, account

    senderType = 'ganache'
    accountAddress = None
    privateKey = None
    if(type(account)==dict):
        accountAddress = account['address']
        privateKey = account['privateKey']
    else:
        accountAddress = account.address
        privateKey = account.privateKey

    # Get sender address from account
    sender =accountAddress
    receiver = request.form.get("receiverAddress")
    amount = request.form.get("amount")

    if(sender == accountAddress):
        senderType = 'newAccountAddress'

    tnxHash= myWallet.makeTransactions(sender, receiver, amount, senderType, privateKey)
    myWallet.addTransactionHash(tnxHash, sender, receiver, amount)
    return redirect("/")

if __name__ == '__main__':
    app.run(debug = True, port=4000)
