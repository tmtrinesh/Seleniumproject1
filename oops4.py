class MyCLass():
    def m1(self):
        print("this is m1 method")
        self.m2(100)

    def m2(self,a):
        print("This is m2 merthos",a)


c1=MyCLass()
c1.m1()