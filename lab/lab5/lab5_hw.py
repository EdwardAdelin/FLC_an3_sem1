#exercitiul 1
#toate linkurile
import re
html=open("HW5Ex1.html", "r").read()
print(re.findall(r'<a href="(.+?)">', html))
#labels of form Last name, First name
labels = re.findall(r'<label[^>]>(.?)</label>', html)
print("Labels:", labels)
#display the types of the attributes in the form (text, number, email)
types = re.findall(r'<input[^>]*type="([^"]+)"', html)
print("Types of Attributes:", types)
#display the values of the options in the form (PhD Student, Professor)
option_texts = re.findall(r'<option[^>]>(.?)</option>', html)
print("Option Texts:", option_texts)
#toate id-urile(lname, fname)
ids = re.findall(r'<input[^>]*id="([^"]+)"', html)
print("IDs in Form:", ids)
print("\n\n")

#2, conversie excel
#pip install  pandas
import pandas as pd
import re
with open("HW5Ex2.txt", "r") as f:
    data_txt = f.readlines()
whole_data = "".join(data_txt)
regex = r'([A-Za-z\s]+)\s*,\s*([A-Za-z]+)\s*,\s*(\d{4}-\d{2}-\d{2})\s*,\s*(\d+)'
matches = re.findall(regex, whole_data)
data = [[m[0].strip(), m[1].strip(), m[2], m[3]] for m in matches]
df = pd.DataFrame(data, columns=["LastName", "FirstName", "HiringDate", "Salary"])
print(df)
#pip install openpyxl
df.to_excel("HW5Ex2.xlsx", index=False)
print("Excel file 'HW5Ex2.xlsx' created successfully.")
print("\n\n")

#ex3
tag_regex = r'<([a-z]+)( [^>])?>.?</\1>'
examples = [
    "<p>Correct</p>",  
    "<p>Unmatched",    
    "p>Missing tag",   
    "<id=incorrect>",  
    "<p>",             
    "<p/>",            
    "<div>Correct</div>", 
]
for example in examples:
    if re.match(tag_regex, example):
        print(f"'{example}' is Correct")
    else:
        print(f"'{example}' is Incorrect")

print("\n\n")

#ex4
def dfa_check(word):
    state = 0
    for char in word:
        if state == 0:
            if char == 'a':
                state = 1
            else:
                state = 3
        elif state == 1:
            if char == 'b':
                state = 2
            else:
                state = 3
        elif state == 2:
            state = 2
        elif state == 3:
            if char == 'a':
                state = 4
            else:
                state = 3
        elif state == 4:
            if char == 'b':
                state = 2
            else:
                state = 3
    return state == 2
#test
words = ["abaa", "aabab", "aabba", "aabb", "cab", "abab"]
for word in words:
    if dfa_check(word):
        print(f"'{word}' e acceptat de DFA")
    else:
        print(f"'{word}' nu e acceptat DFA")