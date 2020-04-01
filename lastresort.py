import csv
import os

def openfile():
    try:
        f = open('siswa.csv', 'r')
        reader = csv.reader(f)
        for row in reader:  
            print (row)
        f.close()
    except FileNotFoundError:
        print("BELUM ADA DATA")

def insertdata():
    print("Masukkan Data Berikut: ")
    innama=input("Nama: ")
    inkelas=input("Kelas: ")
    innilai=input("Nilai: ")
    lst=[innama, inkelas, innilai]

    if os.path.isfile('siswa.csv'):
        f1 = open('siswa.csv', 'a+', newline='' )
        tulis = csv.writer(f1)
        tulis.writerow(lst)
        f1.close()
    else:
        f2 = open('siswa.csv', 'w')
        w = csv.writer(f2) 
        w.writerow(('Nama','Kelas','Nilai'))
        w.writerow(lst)
        f2.close()      


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
        openfile()
    elif selection == '2': 
        insertdata()
    elif selection == '3':
        print ("edit")
    elif selection == '4':
        print ("delete")
    elif selection == '5':
        exit()
    else: 
        print ("Pilihan Tidak dikenal, silahkan ulangi")


