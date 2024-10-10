###__________________________________ex1_________________________________________________________###

list1 = ["Math", "English", "History", "Chemistry", "Biology"]

#nr1
print(list1[1])

#nr2
print(len(list1))

#nr3
print(list1[1:4])

#nr4
print(list1[-4])

#nr5
list2 = list1.copy()
list2.remove("Chemistry")

#nr6
list3 = list1.copy()
list3.insert(2, "Geography")
print(list3)

#nr7
list4 = list1.copy()
list4[list4.index("English")] = "Romanian"
print(list4)

###__________________________________ex2_________________________________________________________###

dict1 = {"Fname" : "Jane", "Lname" : "Doe", "age" : 23}

#ex1
print(dict1["Lname"])

#ex2
dict2 = dict1.copy()
dict2["age"] = 21

#ex3
dict1["occupation"] = "student"

#ex4
dict2 = dict1.copy()
dict2.pop("Fname")

#ex5
print(list(dict1.items()))

#ex6
print(list(dict1.values()))

#ex7
dict1.setdefault("hobby", "chess")
print(dict1)

#ex8
dict1.clear()
print(dict1)

