#Import nessesary plugins
import requests
import json

#linkurl variable is to get the stock.json page
linkurl = requests.get("https://buyvm.hasstock.net/api/stock.json")

#Dumps the objects into jp variable
jp = json.dumps('obj',indent=4)

#jp is to be addresed to pt1 variable
pt1 = jp
pt2 = jp
pt3 = jp

#uses linkurl variable to print out the user defined objects (Line 6)
pt1 = linkurl.json()['1402']
pt2 = linkurl.json()['1414']
pt3 = linkurl.json()['1424']
print(pt1,pt2,pt3)

#user input to exit
input("Press enter to quit")
