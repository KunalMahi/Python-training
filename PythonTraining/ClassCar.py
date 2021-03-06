class Car:
    def SetType(self,type):
        self._Type=type
    def GetType(self):
        return self._Type
    def SetModel(self,model):
        self._Model=model
    def GetModel(self):
        return self._Model
    def SetPrice(self,price):
        self._Price = price
    def GetPrice(self):
        return self._Price
    def SetOwner(self,owner):
        self._Owner = owner
    def GetOwner(self):
        return self._Owner
    def SetMilesDrive(self,milesdrive):
        self._MilesDrive = milesdrive
    def GetMilesDrive(self):
        return self._MilesDrive
    def GetCurrentPrice(self):
        return self.GetPrice()- ( self.GetMilesDrive()*10)

def main():
    mycar=Car()
    mycar.SetType("BMW")
    mycar.SetModel(2015)
    mycar.SetPrice(26000)
    mycar.SetOwner("Kunal")
    mycar.SetMilesDrive(30)
    CurrentPrice=mycar.GetCurrentPrice()
    print("My car's New price={}".format(CurrentPrice))

    Alexcar=Car()
    Alexcar.SetType("BMW")
    Alexcar.SetModel(2016)
    Alexcar.SetPrice(27000)
    Alexcar.SetOwner("Kunal")
    Alexcar.SetMilesDrive(25)
    CurrentPrice = mycar.GetCurrentPrice()
    print("Alex's car's New price={}".format(CurrentPrice))


if __name__ == '__main__':main()

