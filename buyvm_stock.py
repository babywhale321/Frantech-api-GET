import requests
import json

while True:
    
    #connection string
    stockurl = requests.get('https://buyvm.hasstock.net/api/stock.json')

    #pull data from connection string
    data = stockurl.text

    #convert to json format
    jsonparse = json.loads(data)

    #loops through the json data and outputs the value of each vps associated with the name, stock and quantity
    for list in jsonparse:
        print(list,jsonparse[list]['name'],jsonparse[list]['hasStock'],jsonparse[list]['quantity'])

    print("\n")
    input_user = input("Whats the 4 digit code of the KVM you would like to see more data about? 1402 = an example:\n")
    
    #Will first try to parse user defined input into the 4 digit code from the json data
    try:
        name_vps = jsonparse[input_user]['name']
        hasstock_vps = jsonparse[input_user]['hasStock']
        quantity_vps = jsonparse[input_user]['quantity']
        print(name_vps,"Is there stock?",hasstock_vps,"Whats the quantity?",quantity_vps)
        
        #typing 'restart' will restart the program or type anything else will exit the program 
        restart_var = input("Press enter to restart or type the word 'exit' to exit the program\n")
        if restart_var == 'exit': 
            break
        else : 
            continue
    
    #If that fails then it will give some syntax and an option to restart but if they type 'exit' the program exits
    except:
        print("Error, Not a valid code. Please use the first 4 digits on the left of each line. 1520 = an example.")
        ask_var = input("Press enter to restart or type the word 'exit' to exit the program\n")
        if ask_var == 'exit':
            break
        else :
            continue
