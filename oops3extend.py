class MyClass():
    def __init__(self,val1,val2):
        print(val1)
        print(val2)
        self.val1 = val1
        self.val2 = val2

    def add(self):
        print(self.val1 + self.val2)


mc = MyClass(10,20)

mc.add()