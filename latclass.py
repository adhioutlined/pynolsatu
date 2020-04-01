class Car:
    merk = ""
    color = ""

    def __init__(self, color="black", merk="unknown"):
        self.color = color
        self.merk = merk

    def start_enging(self):
        print ("Starting the Car...")
        print ("color: %s" % self.color)
        print ("merk: %s" % self.merk)
        print ("Stop the car...\n\n")


car = Car()
car2 = Car(color="red", merk="Isuju")

car.start_enging()
car2.start_enging()

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("something else went wrong")