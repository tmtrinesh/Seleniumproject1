class Birds:
    def fly(self,name = None):
        if name == "Parrot":
            print("Can fly")
        if name == "Penguine":
            print("Cannot fly")
        if name == None:
            print("No input")


obj = Birds()
obj.fly("Parrot")


class Human:
    def SayHello(self,Name = None):
        if Name is not None:
            print("Hello" +" "  + Name)
        else:
            print("Hello")

obj = Human()
obj.SayHello("Bharani")

class Bank:
    def rateofinterest(self):
        return 0
class ICICI(Bank):
    def rateofinterest(self):
        return 10.5
obj = ICICI()
print(obj.rateofinterest())
obj = Bank()
obj.rateofinterest()


class Myclass:
    __empid = 101

    def getempid(self,eid):
        self.__empid = eid

    def dispempid(self):
        print(self.__empid)

obj = Myclass()
obj.dispempid()
obj.getempid(105)


