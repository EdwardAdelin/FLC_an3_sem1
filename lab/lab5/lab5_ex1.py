def dfa_ones(word):
    state = 'A'
    for char in word:
        if state == 'A':
            if char == '1':
                state = 'A'  
            else:
                state = 'B'  
        elif state == 'B':
            break
    return state == 'A'


print(dfa_ones("111")) #true
print(dfa_ones("1110")) #false