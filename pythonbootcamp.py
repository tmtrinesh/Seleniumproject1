#friends = ["jim", "carry", "Harry"]
#for friend in friends:
 #   print(friend)
#for index in range(0,10,1):
#    print(index)

#for index in range(len(friends)):
#    print(friends[index])
#for index in range(5):
 #   if index == 0:
 #       print("First iteration")
  #  else:
      #  print("Not first")

#def raise_to_power(base_num , pow_num):
#    result = 1
 #   for index in range(pow_num):
 #      result = result*base_num
 #   return result
#print(raise_to_power(2,3))

#number_grid = [
 #   [1,2,3],
   # [4,5,6],
   # [7,8,9],
   # [0]
#]
#print(number_grid[0][0])
#for row in number_grid:
 #   for col in row:
  #      print(col)
  #  print(row)

#def translate(phrase):
 #   translation= ""
  #  for letter in phrase:
   #     if letter in "AEIOUaeiou":
    #        translation = translation + "g"
     #   else:
      #      translation = translation + letter
    #return translation
#print(translate(input(";Enter a phrse:")))
''' try:
    number = int(input("Enter Number:"))
    print(number)
except:
    print("Invalid input")'''

#from student import Student

#student1 = Student("jiom","business",3.1,False)
#print(student1.name)

#string_to_iterate = "Data Science"
#for char in string_to_iterate[: : -1]:
#    print(char)

#string_to_iterate = "Data Science"
#for char_index in range(len(string_to_iterate)):
   #print(string_to_iterate[char_index])


#string_to_iterate = "Machine Learning"
#char_index = len(string_to_iterate) - 1
#while char_index >= 0:
  #    print(string_to_iterate[char_index])
      #char_index -= 1

#string_to_iterate = "Learn Python"
#char_index = 1
#while char_index <= len(string_to_iterate):
 #     print(string_to_iterate[-char_index])
     # char_index += 1


#def myfunc(text, num):
 #  while num > 0:
  #   num = num - 1

#myfunc('Hello', 4)


#def func(x=1, y=2):
 #  x = x + y
 #  y += 1
 #  print(x, y)


#func(x=1, y=2)



#num = 1
#def func():

  #  num = num + 3
    #print(num)

#func()
#print(num)



name= "Trinesh"
Age= 29
Class= 123456

print(name,Age,Class)