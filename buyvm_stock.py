import requests
import json

#connection string
stockurl = requests.get('https://buyvm.hasstock.net/api/stock.json')

#pull data from connection string
data = stockurl.text

#convert to json format
jsonparse = json.loads(data)

#1GB Selectors
name_1411 = jsonparse['1411']['name']
hasstock_1411 = jsonparse['1411']['hasStock']
quantity_1411 = jsonparse['1411']['quantity']

name_1413 = jsonparse['1413']['name']
hasstock_1413 = jsonparse['1413']['hasStock']
quantity_1413 = jsonparse['1413']['quantity']

name_1423 = jsonparse['1423']['name']
hasstock_1423 = jsonparse['1423']['hasStock']
quantity_1423 = jsonparse['1423']['quantity']

#2GB Selectors
name_1402 = jsonparse['1402']['name']
hasstock_1402 = jsonparse['1402']['hasStock']
quantity_1402 = jsonparse['1402']['quantity']

name_1414 = jsonparse['1414']['name']
hasstock_1414 = jsonparse['1414']['hasStock']
quantity_1414 = jsonparse['1414']['quantity']

name_1424 = jsonparse['1424']['name']
hasstock_1424 = jsonparse['1424']['hasStock']
quantity_1424 = jsonparse['1424']['quantity']

#prints the selectors
#name is the location/size and hasstock is true or false
print("1GB Ram")
print(name_1411,"Stock?",hasstock_1411,"Quanity?",quantity_1411)
print(name_1413,"Stock?",hasstock_1413,"Quanity?",quantity_1413)
print(name_1423,"Stock?",hasstock_1423,"Quanity?",quantity_1423)
print("\n")
print("2GB Ram")
print(name_1402,"Stock?",hasstock_1402,"Quanity?",quantity_1402)
print(name_1414,"Stock?",hasstock_1414,"Quanity?",quantity_1414)
print(name_1424,"Stock?",hasstock_1424,"Quanity?",quantity_1424)
print("\n")
input("Press enter to quit")
