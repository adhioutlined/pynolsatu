par="NolSatu hadir sebagai usAha untuk merespon masalah bersama yaitu banyak lulusan teknologi informatika atau profesional teknologi informatika yang kemampuannya kuranG sementara perusahaan-perusahaan membutuhkan profesional teknologi informatika terbaik dengan kemampuan terkini. Selain itu, perkembangan teknologi informatika global Berlangsung sangat cepat dan kemampuan profesional teknologi informatika disarankan selaras dengan perkembangan tersebut. Profesional teknologi informatika diharapkan dapat membantu perusahaan dalaM mengadopsi teknologi informatika terkini untuk mendOrong proses bisnis perusahaan. Imbal balik bagi profesional teknologi informatika dari proses ini adalah penghasilan yang cukup dan kesejahteraAN yang baik yang diberikan oleh perusahaaN. NolSatu adalah media untuk Talenta teknologi informatika dilatih agar memiliki kemampuan terkini kemudian disalurkan ke perusahaan yang membutuhkan. NolSatu juga media untuk Profesional teknologi informatika dilatih agar kemampuannya termutakhirkan kemudian disalurkan ke perusahaan baru yang membutuhkan."

## SOAL1
soal1=sum(1 for c in par if c.isupper())
print("1. Berapa banyak huruf kapital? ", soal1)

## SOAL2
soal2=par.split(" ")
print("2. Ada berapa kata dalam paragraf? ", len(soal2))

## SOAL3
soal3=par.split(". ")
print("3. Ada berapa kalimat? ", len(soal3))

## SOAL4
soal4=[]
parlow=par.lower()
parlow2=parlow.rstrip(".")
pars=parlow2.split(". ")

for elem in pars:
    if elem.startswith("nolsatu") and elem.endswith("membutuhkan"):
        soal4.append(elem)

print("4. Ada berapa kalimat yang diawali dengan kata 'nolsatu dan diakhiri dengan kata membutuhkan'?", len(soal4))

## SOAL5
print("5. Ubah setiap kalimat menjadi capitalize.")
soal5=[]
pars5=par.split(". ")
for c in pars5:
    soal5.append(c.capitalize())

print('. '.join(soal5))