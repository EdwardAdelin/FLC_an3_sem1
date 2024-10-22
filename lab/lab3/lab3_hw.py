#########################__ex1__#########################
#Create your own module with any function you want and use it in another
#file.

import modules_hw
add_numbers = modules_hw.add_numbers
print(add_numbers(5, 6))

#########################__ex2__#########################
#Create a list populated with 5 random numbers (Hint: use randint())

from random import randint
list_of_random_numbers = [randint(0, 100) for i in range(5)]

#########################__ex3__#########################
#Write a function that prints a list of 5 random integers between 40 and 70.

function = lambda: [randint(40, 70) for i in range(5)]

#########################__ex4__#########################
#Use the datetime module to create a datetime object and print the full name
#of the weekday of that day.

from datetime import datetime
import os
datetime_object = datetime.now()
print(datetime_object.strftime("%A"))

#########################__ex5__#########################
#Create a directory. Create a.txt file in it. Add some text to it. Read the first 2
#lines. Overwrite the text inside the file.

# Create directory
directory = "directory_ex5_hw"
if not os.path.exists(directory):
    os.makedirs(directory)

# Define the file path
file_path = os.path.join(directory, "file.txt")

# Write initial text to the file
initial_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
with open(file_path, "w") as file:
    file.write(initial_text)

# Read the first 2 lines
with open(file_path, "r") as file:
    lines = [file.readline().strip() for _ in range(2)]
    print("First 2 lines:", lines)

# Overwrite the text inside the file
with open(file_path, "w") as file:
    file.write(str(lines))

#########################__ex6__#########################
#Print the name of the operating system. List the files and directories in the
#current directory.

print("Operating system:", os.name)
print("Files and directories in the current directory:", os.listdir())

#########################__ex7__#########################
#Write a program that displays the date that was 10days before the current
#date.

from datetime import timedelta
ten_days_ago = datetime.now() - timedelta(days=10)
print("10 days ago:", ten_days_ago.strftime("%Y-%m-%d"))



