def hello(x, y, z, **kwargs):
    print(x)
    print(y)
    print(z)
    print(kwargs)

hello(1, 2, 3, a=4)
hello(1, 2, 3, a=4, b=5)


def hello2(x, y, z, *args):
    print(x)
    print(y)
    print(z)
    print(args)

hello2(1, 2, 3, 4)
hello2(1, 2, 3, 4, 5)
hello2(1, 2, 3, 4, 5, 6)


def jumlah(x, y):
    result = x + y
    return result

hasil = jumlah(10, 5)
print(hasil)