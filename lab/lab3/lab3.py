#exercitiul 1
#Write a program that displays the current date and time with the
#complete name of the month. (Hint: use datetime.now())

import datetime
import calendar
now = datetime.datetime.now()
month_name = calendar.month_name[now.month]
print(f"{now.day} {month_name} {now.year} {now.hour}:{now.minute}:{now.second}")

#exercitiul 2
#Write a program that takes as user input the radius of a circle (as an
#integer) and displays the area of that circle. 𝐴 = 𝜋𝑟^2

import math
r = int(input("Enter the radius of the circle: "))
A = math.pi * r**2
print(f"The area of the circle is: {A}")

#exercitiul 3
#Select a random number from a list. (Hint: use random.choice())
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
import random
print(f"Random choice of list is: {random.choice(list)}")

#exercitiul 4
#Shuffle the elements from a given list. (Hint: use random.shuffle())

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(list)
print(f"Shuffled list is: {list}")

#exercitiul 5
# Use the math module to compute the least common multiple and the
# greatest common divisor of two numbers.

import math
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"The least common multiple of {a} and {b} is: {math.lcm(a, b)}")
print(f"The greatest common divisor of {a} and {b} is: {math.gcd(a, b)}")

#exercitiul 6
# Use the math module to compute the factorial of a number inputted by
# the user

import math
n = int(input("Enter a number: "))
print(f"The factorial of {n} is: {math.factorial(n)}")

#exercitiul 7
# Write a program that displays the week number of a date. (Hint: use
# isocalendar())

import datetime
now = datetime.datetime.now()
print(f"The week number of the date is: {now.isocalendar()[1]}")

#exercitiul 8
#Write a program that computes the distance between two points.

import math
x1 = int(input("Enter the x coordinate of the first point: "))
y1 = int(input("Enter the y coordinate of the first point: "))
x2 = int(input("Enter the x coordinate of the second point: "))
y2 = int(input("Enter the y coordinate of the second point: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"The distance between the two points is: {distance}")




