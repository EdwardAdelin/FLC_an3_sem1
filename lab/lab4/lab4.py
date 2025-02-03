#ex1
# a=“rectangle”, b=“square”, c=“sphere”, d=“triangle”, e=“cone”, f=“cube”, g=“cylinder”. Using
# compile(), print only the strings that start with either c or s and end with e.

import re
strings = ["rectangle", "square", "sphere", "triangle", "cone", "cube", "cylinder"]
pattern = re.compile(r"[cs].*e")
matching_shapes = [strings for strings in strings if pattern.match(strings)]
print(matching_shapes)

#ex2
# words=“car, cat, dog, pool, bath, cone, cube, ring, int”. Write a regex that prints only the words
# that have exactly 4 letters.

words = "car, cat, dog, pool, bath, cone, cube, ring, int"
pattern = re.compile(r"\b\w{4}\b")
matching_words = [word for word in words.split(", ") if pattern.match(word)]
print(matching_words)

#ex3
# list=[“square”,”triangle”,”cube”,”sphere”,”circle”,”pentagon”, “hexagon”,
# “rectangle”,”parallelogram”,”trapezoid”]. Loop thourgh the list 
# and match only the words ending in
# “re”.

words = ["square", "triangle", "cube", "sphere", "circle", "pentagon", "hexagon", "rectangle", "parallelogram", "trapezoid"]
pattern = re.compile(r"re$")
matching_words = [word for word in words if pattern.match(word)]
print(matching_words)

#ex4
# Take the list from the previous exercise and search for the words in it in the string: geo=“A square
# has 4 sides, a triangle has 3, a pentagon has 5, a hexagon has 6. While a square has 4 equal sides, a
# triangle can have 0, 2 or 3 equal sides.”. Extract from geo the digits and the non-digits characters.

geo = "A square has 4 sides, a triangle has 3, a pentagon has 5, a hexagon has 6. While a square has 4 equal sides, a triangle can have 0, 2 or 3 equal sides."
pattern = re.compile(r"\b\w+\b")
matching_words = [word for word in words if pattern.match(word)]
print(matching_words)

#ex5
#link=“https://www.newyorker.com/magazine/2021/11/01/the-book-of-form-and-emptiness-thewar-for-gloria-read-until-you-understand-and-the-end-of-bias”. Extract the year, month and date
# from ex2.

link = "https://www.newyorker.com/magazine/2021/11/01/the-book-of-form-and-emptiness-thewar-for-gloria-read-until-you-understand-and-the-end-of-bias"
pattern = re.compile(r"\d{4}/\d{2}/\d{2}")
matching_date = pattern.search(link)
print(matching_date.group())

#ex6
#date= "2021-11-02“. Change the date format to DD-MM-YYYY

date = "2021-11-02"
pattern = re.compile(r"\d{4}-\d{2}-\d{2}")
matching_date = pattern.search(date)
print(matching_date.group())
date = matching_date.group().split("-")
date = "-".join(date[::-1])
print(date)

#ex7
#Write a function to check if a string starts with a digit. 
# Provide at least two examples (one right and
# one wrong).

def starts_with_digit(string):
    pattern = re.compile(r"^\d")
    return pattern.match(string) is not None

print(starts_with_digit("1abc"))
print(starts_with_digit("abc1"))

#ex8
# Write a function to check if a string ends with a digit. 
# Provide at least two examples when calling
# the function (one right and one wrong).

def ends_with_digit(string):
    pattern = re.compile(r"\d$")
    return pattern.match(string) is not None

print(ends_with_digit("abc1"))
print(ends_with_digit("1abc"))

#ex9
# Write a function to check if a string contains a digit. 
# Provide at least two examples (one right and
# one wrong). 

def contains_digit(string):
    pattern = re.compile(r"\d")
    return pattern.search(string) is not None

print(contains_digit("abc1"))
print(contains_digit("abc"))

#end of lab4.py