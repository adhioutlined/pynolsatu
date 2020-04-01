import csv
import os



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
    

#  
#  try:
    #  f1 = open('siswa.csv', 'a+', newline='' )
    #  tulis = csv.writer(f1)
    #  tulis.writerow(lst)
    #  f1.close()
#  except FileNotFoundError:
    #  f2 = open('siswa.csv', 'w')
    #  w = csv.writer(f2) 
    #  w.writerow(('Nama','Kelas','Nilai'))
    #  w.writerow(lst)
    #  f2.close()
    

