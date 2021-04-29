class Emp:
    def __init__(self,eid,ename,sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal

    def display(self):
        print("Empid:%d Empname:%s Empsal:%g"%(self.eid,self.ename,self.sal))
        #format(self.eid,self.ename,self.sal)

e1=Emp(101,'Smith',10000)
e1.display()