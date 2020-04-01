menu = {}
menu['1']="Show Data" 
menu['2']="Insert Data"
menu['3']="Edit Data"
menu['4']="Delete Data"
menu['5']="Exit"
while True: 
    options=menu.keys()
#    options.sort()
    print ("----------- MENU ----------")
    for entry in options: 
        print (entry, menu[entry])
    selection=input("Please Select:") 
    if selection =='1': 
        print ("Show") 
    elif selection == '2': 
        print ("delete")
    elif selection == '3':
        print ("find")
    elif selection == '5': 
        break
    else: 
        print ("Unknown Option Selected!")