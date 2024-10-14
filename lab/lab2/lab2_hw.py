##########exercise1###########################################################################

#Write a function that prints the Fibonacci series based on the number of terms
#inputted by the user (e.g., if the user inputs 5, the output should be 0 1 1 2 3)

# def fibonacci(n):
#     if n==1:
#         print(0)
#     if n==2:
#         print(1)
#     else:
#         print(0)
#         print(1)
#         a = 0
#         b = 1
#         for i in range (0,n-2):
#             print(a+b)
#             variable=a+b
#             a=b
#             b=variable

# fibonacci(5)


##########exercise2###########################################################################

#Write a function that computes the great common divisor of two positive numbers.

# print("Insert two positive numbers, to find their greatest common divisor")

# number1 = int(input("Write first number: "))
# number2 = int(input("Write second number: "))

# max_possible_divisor=min(number1, number2)
# greatest_common_divisor=1 #default maximum common divisor for any two numbers

# for i in range (2, max_possible_divisor+1):
#     if number1%i==0 and  number2%i==0:
#         greatest_common_divisor=i

# print("Greatest common divisor of "+str(number1)+" and  "+str(number2)+" is: "+str(greatest_common_divisor))



##########exercise3###########################################################################

#Write a function that computes the least common multiple of two positive
#numbers. 

# import math

# print("Insert the numbers to find Lowest Common Multiple!")
# num1 = int(input("Insert a: "))
# num2 = int(input("Insert  b: "))

# def lcm(a, b):
#     return abs(a * b) // math.gcd(a, b)

# print(f"LCM of {num1} and {num2} is {lcm(num1, num2)}")


##########exercise4###########################################################################

# Write a function that takes as input a list of integers and returns 2 lists: one with
# the even numbers from the initial list and on with the odd numbers (e.g.,
# list1=[1,2,3,4,5,6], the lists obtained using the function will be listEven=[2,4,6]
# and listOdd=[1,3,5])

# print("Insert numbers into the list (to splint into even and odd) : ")
# list =  [1,2,3,4,5,6]
# list_even = [] #par
# list_odd = [] #impar
# for i in range  (0, len(list)):
#     if (list[i]%2==0):
#         list_even.append(list[i])
#     if (list[i]%2!=0):
#         list_odd.append(list[i])
# print("Even list is: " + str(list_even))
# print("Odd list is: " + str(list_odd))

##########exercise5###########################################################################

# Write a program which has a class called “Cube” constructed by the length of one
# side and 3 functions which will compute: the area of one surface, the area of all
# surfaces and the volume of the cube.

# class Cube:
#     def __init__(self, side_length):
#         self.side_length = side_length

#     def surface_area_one(self):
#         return self.side_length ** 2

#     def surface_area_all(self):
#         return 6 * self.surface_area_one()

#     def volume(self):
#         return self.side_length ** 3

# # Example usage:
# cube = Cube(3)
# print(f"Area of one surface: {cube.surface_area_one()}")
# print(f"Area of all surfaces: {cube.surface_area_all()}")
# print(f"Volume of the cube: {cube.volume()}")

##########exercise6###########################################################################

# Write a program using lambda that will get the power of a specified number.
# (e.g., power of 2/3 of the specified number 5 will output 25/125)

# number = 5
# power_of_2 = lambda x: x ** 2
# power_of_3 = lambda x: x ** 3
    
# print(f"Power of 2 of {number} is {power_of_2(number)}")
# print(f"Power of 3 of {number} is {power_of_3(number)}")

##########end_of_homework###########################################################################

    
    
            


