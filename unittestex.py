#s="Hi"
#print (s[1])
#print(s[:1])
#print(len(s))
#print (s +  " ther")
#print("trinesh")
#print("   /|")
#print("  / |")
#print(" /  |")
#print("/___|")

#character_name = "ABC"
#character_age =  "90.89095456"
#is_male = False
#pint("There once a man named " + character_name +","   )
#print("He was "  + character_age + " years old.")

#character_name = "Jack"
#print("he  dislikes the name " + character_name + ",")
#print("but he didnt like being "  + character_age + ".")
#print("Giraffe\nAcademy")
from math import *
#phrase = "Giraffe Academy"
#print(phrase  + " is cool")
#print(phrase.upper().isupper())
#print(len(phrase))
#print(phrase[0])
#print(phrase.index("a"))
#print(phrase.replace("Giraffe","Trinesh"))

#working with number
#my_num = 5
#print(str(my_num) + " is my favourite number")
#print(abs(my_num))
#print(pow(5,2))
#print(max(98,87))
#print(min(8,87))
#print(round(8.87))
#print(ceil(8.87))
#print(floor(8.87))
#name = input("Enter your name:")
#age = input("Enter your age:")
#print("Hello " +  name  +" ! you are " + age )
#color = input("Enter a color:")
#plural_noun = input("Enter plural noun:")
#celebrity = input("Enter a celebrity:")
#print("Roses are" + color)
#print(plural_noun + " are blue")
#print("I love " + celebrity)
#lucky_numbers =[1,3,6,8,9]
#Friends =["trinesh","jack","Mike","carry","harry" ]


#Friends[1]= "Trinn"
#print(len(Friends))
#Friends.insert(2,"jimmy")
#Friends.append("creed")
#Friends.remove("Mike")
#Friends.extend(lucky_numbers)
#Friends.pop()
#print(Friends.index("harry"))
#lucky_numbers.sort()
#lucky_numbers.reverse()
#lucky_numbers2=lucky_numbers.copy()
#print(lucky_numbers2)

#print(len(Friends))
#x=[(1,3,36,78),(2,3),(1,4)]
#print(x[0:])
#functions
#def say_Hi(name):
 #   print("Hello world " + name)
#print("Hi trinesh")
#say_Hi("Trinesh")
#say_Hi("Jack")
#say_Hi("Tony")
#print("its bottom")

#def cube(num):
 #   return num*num*num
#result = cube(4)
#print(result)

#is_male = False
#is_tall = True
#if is_male or is_tall:
#    print("you are a tall male ")
#elif is_male and not (is_tall):
  #  print("you are a short male")
#elif not (is_male) and (is_tall):
  #  print("you are tall female")
#else:
 #   print("you are niether male nor tall")

#def max_num(num1,num2,num3):
 ##      return num1
 #    elif num2 >= num3 and num2 >= num1:
  #       return num2
    # else:
   #      return num3



#print(max_num(2,45,72))


#num1 = float(input("Enter a first number:"))
#op = input("Enter operator:")
#num2 = float(input("Enter a second number:"))
#if op == "+":
#    print(num1+num2)
#elif op == "-":
#    print("num1-num2")
#elif op == "/":
#    print("num1/num2")
#elif op == "*":
 #   print("num1*num2")
#else:
 #   print("invalid operator")


#monthConversions = {
 #   "Jan": "January",
  #  "Feb": "February",
   # "Mar": "March",}
#print(monthConversions.get("Mar"))

#While loop


#i = 1
#while i<=10:
#    print(i)
  #  i += 1
#print("Done with loop")
secret_world = "Giraffe"
Guess = ""
Guess_count = 0
Guess_limit = 3
out_of_Guesses =False
while Guess != secret_world and  not (out_of_Guesses):
    if Guess_count < Guess_limit:
        Guess = input("Enter the Guess:")
        Guess_count += 1
    else:
        out_of_Guesses = True
if out_of_Guesses:
    print("out of guesses you lose")
else:
    print("You win")
