class A:
    a, b = 10, 20


class B(A):
    i, j = 100, 200

    def m1(self, a, b):
        print(a+ b)
        print(self.i + self.j)
        print(self.a + self.b)


b = B()
b.m1(1, 2)