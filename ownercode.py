from web3 import Web3
import json

#Connect to Ganache
def OwnerAgree():
	w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

	#Get smart contract address
	file=open("smartcontract_address.txt", "r")
	cont_addr=file.read()
	file.close()

	abi=json.load(open("smartcontract_abi.json","r")) #get ABI

	contract = w3.eth.contract(address=cont_addr, abi=abi)

	account = w3.eth.accounts[0] 
	account2=w3.eth.accounts[1] 

	#params:  owner address, customer address, car id
	tx_hash = contract.functions.setRenters(account, account2, 1).transact({'from': account})
	w3.eth.wait_for_transaction_receipt(tx_hash)

	rentinfo = contract.functions.getRenters().call({'from': account}) #Call is better for reading, transact for writing to the blockchain
	print(rentinfo)


def CustomerAgree():
	w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

	#Get smart contract address
	file=open("smartcontract_address.txt", "r")
	cont_addr=file.read()
	file.close()

	abi=json.load(open("smartcontract_abi.json","r")) #get ABI

	contract = w3.eth.contract(address=cont_addr, abi=abi)

	account = w3.eth.accounts[0] 
	account2=w3.eth.accounts[1] 

	#params:  owner address, customer address, car id
	tx_hash = contract.functions.setRenters(account, account2, 1).transact({'from': account2})
	w3.eth.wait_for_transaction_receipt(tx_hash)

	rentinfo = contract.functions.getRenters().call({'from': account2}) #Call is better for reading, transact for writing to the blockchain
	print(rentinfo)

def CustomerPay(amount=10):
	w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

	#Get smart contract address
	file=open("smartcontract_address.txt", "r")
	cont_addr=file.read()
	file.close()

	abi=json.load(open("smartcontract_abi.json","r")) #get ABI

	contract = w3.eth.contract(address=cont_addr, abi=abi)

	account = w3.eth.accounts[0] 
	account2=w3.eth.accounts[1] 
	amount=w3.to_wei(amount, 'ether')

	#params:  owner address, customer address, car id
	tx_hash = contract.functions.sendEth(amount).transact({'from': account2,'value': amount})
	w3.eth.wait_for_transaction_receipt(tx_hash)
	print(str(amount)+" Eth was transfered from customer to owner")

OwnerAgree()
CustomerAgree()
CustomerPay(13)
