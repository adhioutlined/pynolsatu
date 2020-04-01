def fibonacci(bil):
  fibmin1 = 0
  fibmin2 = 0
  fibh = 0
  for x in range(1,bil+1):
    fibmin2 = fibmin1
    fibmin1 = fibh
    if x<=0:
      fibh = 0
    elif x<=2:
      fibh = 1
    else:
      fibh = fibmin1 + fibmin2
  return fibh

angka = int(input('Cari Fibonacci ke- '))
fib_bil = fibonacci(angka)
print(fib_bil)