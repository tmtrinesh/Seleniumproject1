num=7777
count=0


if num>1:
    for i in range(1,num+1):
        if (num%i)==0:
            count=count+1
    if count==2:
        print("num is prime")
    else:
        print("num is not prime")
#number which is divisible by 1 and itself
#which is have only 2 faCTORS        