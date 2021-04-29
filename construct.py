class A:
    def __init__(self):
        print("Constructor from A")

class B(A):
    def __init__(self):
        print("Constructor from B")
        super(B, self).__init__()
        A.__init__(self)

    pass



bobj=B()


class MyClass():
    def m2(self):
        print("Good morning Trinesh")

    def __init__(self):
        print("thjis is constructor")


C = MyClass()
C.m2()
