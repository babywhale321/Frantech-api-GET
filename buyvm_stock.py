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

name_1413 = jsonparse['1413']['name']
hasstock_1413 = jsonparse['1413']['hasStock']

name_1423 = jsonparse['1423']['name']
hasstock_1423 = jsonparse['1423']['hasStock']

#2GB Selectors
name_1402 = jsonparse['1402']['name']
hasstock_1402 = jsonparse['1402']['hasStock']

name_1414 = jsonparse['1414']['name']
hasstock_1414 = jsonparse['1414']['hasStock']

name_1424 = jsonparse['1424']['name']
hasstock_1424 = jsonparse['1424']['hasStock']

#prints the selectors
#name is the location/size and hasstock is true or false
print("1GB")
print(name_1411,hasstock_1411)
print(name_1413,hasstock_1413)
print(name_1423,hasstock_1423)
print("\n")
print("2GB")
print(name_1402,hasstock_1402)
print(name_1414,hasstock_1414)
print(name_1424,hasstock_1424)
print("\n")
input("Press enter to quit")
