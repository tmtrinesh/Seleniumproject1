#num1=10
#num2=20


num1= input("Enter the value of num1")
num2= input("Enter the value of num2")


print("Value of num1 before swapping",num1)
print("Value of num2 before swapping",num2)

#temp=num1
#num1=num2
#num2=temp

num1,num2 = num2,num1
print("Value of num1 after swapping",num1)
print("Value of num2 after swapping",num2)
