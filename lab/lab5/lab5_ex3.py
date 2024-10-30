def dfa_start_end_same(word):
    if len(word) < 1:
        return False
    start_char = word[0]
    return word[-1] == start_char


print(dfa_start_end_same("abba"))  #false
print(dfa_start_end_same("abcd")) #false