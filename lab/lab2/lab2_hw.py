#exercise1
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

#exercise2
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

#exercise3
#Write a function that computes the least common multiple of two positive
#numbers. 

# import math

# print("Insert the numbers to find Lowest Common Multiple!")
# num1 = int(input("Insert a: "))
# num2 = int(input("Insert  b: "))

# def lcm(a, b):
#     return abs(a * b) // math.gcd(a, b)

# print(f"LCM of {num1} and {num2} is {lcm(num1, num2)}")

#exercise4
# Write a function that takes as input a list of integers and returns 2 lists: one with
# the even numbers from the initial list and on with the odd numbers (e.g.,
# list1=[1,2,3,4,5,6], the lists obtained using the function will be listEven=[2,4,6]
# and listOdd=[1,3,5])

print("Insert numbers into the list (to splint into even and odd) : ")




    
    
            


