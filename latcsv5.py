import csv

siswa = [

    ('alan', 'A', 90),

    ('tayo', 'B', 85),

    ('xapi', 'A', 80),

    ('leon', 'B', 90),

    ('nima', 'C', 70)

]


with open('siswa.csv', 'w') as f:  
    w = csv.writer(f)
    w.writerow(('jeto','D','100'))