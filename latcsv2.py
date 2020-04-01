import csv
try:
    f = open('siswa.csv', 'r')
    reader = csv.reader(f)
    for row in reader:  
        print (row)
    f.close()
except FileNotFoundError:
    print("BELUM ADA DATA")

