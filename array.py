numList = []
print ("Masukkan angka-angka yang akan dihitung rata-rata, akhiri dengan x")
while True:
    app = input("angka : " )

    if app == 'x':
        avg = sum(numList)/len(numList)
        print("Nilai rata-rata angka diatas adalah : ", (avg))
        break
    else:
        int_app = int(app)
        numList.append(int_app)
