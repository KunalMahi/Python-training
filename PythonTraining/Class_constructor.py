class Car:
    def __init__(self,type,model,price,owner,milesdrive):
        self._Type=type
        self._Model=model
        self._Price=price
        self._MilesDrive=milesdrive
        self._Owner=owner
    def GetType(self):
        return self._Type
    def GetModel(self):
        return self._Model
    def GetPrice(self):
        return self._Price
    def GetOwner(self):
        return self._Owner
    def GetMilesDrive(self):
        return self._MilesDrive
    def GetCurrentPrice(self):
        return self.GetPrice()- ( self.GetMilesDrive()*10)

def main():
    mycar=Car("BMW",2015,26000,"Kunal",30)
    CurrentPrice=mycar.GetCurrentPrice()
    print("{}'s car's New price={}".format(mycar._Owner,CurrentPrice))

    Alexcar=Car("BMW",2016,27000,"Alex",25)
    CurrentPrice = mycar.GetCurrentPrice()
    print("{}'s car's New price={}".format(Alexcar._Owner,CurrentPrice))


if __name__ == '__main__':main()

