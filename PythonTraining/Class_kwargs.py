class Car:
    def __init__(self,**kwargs):
        self._Data=kwargs
    def GetType(self):
        return self._Data["Type"]
    def GetModel(self):
        return self._Data["Model"]
    def GetPrice(self):
        return self._Data["Price"]
    def GetOwner(self):
        return self._Data["Owner"]
    def GetMilesDrive(self):
        return self._Data["MilesDrive"]
    def GetCurrentPrice(self):
        return self.GetPrice()- ( self.GetMilesDrive()*10)

def main():
    mycar=Car(Type="BMW",Model=2015,Price=26000,Owner="Kunal",MilesDrive=30)
    CurrentPrice=mycar.GetCurrentPrice()
    print("{}'s car's New price={}".format(mycar._Data["Owner"],CurrentPrice))

    Alexcar=Car(Type="BMW",Model=2016,Price=27000,Owner="Alex",MilesDrive=25)
    CurrentPrice = mycar.GetCurrentPrice()
    print("{}'s car's New price={}".format(Alexcar._Data["Owner"],CurrentPrice))


if __name__ == '__main__':main()

