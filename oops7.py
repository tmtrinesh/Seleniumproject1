class Myclass:
    pass
c=Myclass()
print(c)


class Myclass1:
    def __str__(self):
        return "welcome"

d=Myclass1()
print(d)



def sum(start,end):
    result =0
    for i in range(start,end+1):
        result = result+i
        print(result)
sum(10,20)