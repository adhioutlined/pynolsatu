menu = {}
menu['1']="Show Data" 
menu['2']="Insert Data"
menu['3']="Edit Data"
menu['4']="Delete Data"
menu['5']="Exit"
while True: 
    options=menu.keys()
    print ("----------- MENU ----------")
    for entry in options: 
        print (entry, menu[entry])
    selection=input("Pilih Nomor Menu:") 
    if selection =='1': 
        print ("Show") 
    elif selection == '2': 
        print ("insert data")
    elif selection == '3':
        print ("edit")
    elif selection == '4':
        print ("delete")
    elif selection == '5':
        exit()
    else: 
        print ("Pilihan Tidak dikenal, silahkan ulangi")