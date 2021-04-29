def sum(*args):
    s = 0
    for  i in args:
        s+=i
    print("Sum is", s)
sum(1,2)
sum(1,2,3)

x = lambda a :a+10
print(x(5))

t1 = ()
t2 = (11,25,46)
t3 = ([1,2,3,3,4,5,6,9])
t4 = tuple("abc")
list = [1,2,3,3,4,5,6,9]


print(t4)
print(t3)
print(list)
