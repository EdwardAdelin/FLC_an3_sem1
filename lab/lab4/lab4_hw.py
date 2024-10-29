import re
from datetime import datetime

# 1. Funcție pentru verificarea dacă un string conține doar litere mici, cifre și *
def check_lowercase_digits_star(s):
    return bool(re.fullmatch(r"[a-z0-9*]+", s))

print(check_lowercase_digits_star("abc123*"))  
print(check_lowercase_digits_star("Abc123*"))  

# 2. Funcție ce verifică dacă string-ul are un cuvânt mare _ cuvânt mic
def check_pattern(s):
    return bool(re.fullmatch(r"[A-Z]+_[a-z]+", s))

print(check_pattern("FILS_student"))  
print(check_pattern("Fils_Student"))  

# 3. Lista de cuvinte și filtrarea după "le" sau "re"
hw4 = "rectangle square sphere triangle cone cube cylinder"
words = hw4.split()
# Filtrează doar cuvintele cu sfârșit corect
print([word for word in words if word.endswith(("le", "re"))])

# 4. Regex cu două grupuri și afișarea tuturor potrivirilor
text = "FILS_student and UNIVERSITY_class"
pattern = r"([A-Z]+)_([a-z]+)"
matches = re.finditer(pattern, text)

# Afișează toate potrivirile
for match in matches:
    print("Match:", match.group(0))  
    print("Grup 1:", match.group(1)) 
    print("Grup 2:", match.group(2)) 

# 5. Schimbarea formatului datei
def change_date_format(date_str):
    date_obj = datetime.strptime(date_str, "%y-%m-%d")
    # Scoate noul format cu luna scrisă
    return date_obj.strftime("%d-%B-%y")

print(change_date_format("21-12-01"))  # Rezultat: 01-December-21

# 6. Funcție care verifică un text ce începe cu "m", termină cu "n" și are fix 3 caractere între
def match_m_n(s):
    return bool(re.fullmatch(r"m...n", s))

print(match_m_n("moon"))  
print(match_m_n("mooon")) 

# 7. Funcție care potrivește textul ce începe cu "h" și are exact 2 sau 3 "i"
def match_hi(s):
    return bool(re.fullmatch(r"hi{2,3}", s))

print(match_hi("hii"))  
print(match_hi("hiiii")) 

# 8. Funcție ce potrivește cuvintele cu "q" dar nu la început sau la sfârșit
def match_q_not_edges(s):
    return bool(re.search(r"\Bq\B", s))

print(match_q_not_edges("faqed"))  
print(match_q_not_edges("quick"))   

# 9. Funcție care înlocuiește "a" cu "u" și "i" cu "e" într-un text
def replace_a_i(text):
    return text.replace("a", "u").replace("i", "e")

print(replace_a_i("an amazing idea")) 
