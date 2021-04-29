class A:
    def m1(self):
        print("This is method from A")


class B(A):
    def m2(self):
        print("This is method from B")
        super().m1()

b=B()

b.m2()


