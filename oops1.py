class A:
    a,b =10,20


class B(A):
    a,b=100,200


    def m1(self,a,b):
        print(a+b)
        print(super().a + super().b)
        print(self.a + self.b)
       


bobj=B()
bobj.m1(1,2)