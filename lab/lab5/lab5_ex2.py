def dfa_even_zeros_one(word):
    state = 'A'
    for char in word:
        if state == 'A':
            state = 'B' if char == '0' else 'G'
        elif state == 'B':
            state = 'C' if char == '0' else 'G'
        elif state == 'C':
            state = 'D' if char == '1' else 'B'
        elif state == 'D':
            if char != '1':
                state = 'G'
        elif state == 'G':
            break
    return state == 'D'


print(dfa_even_zeros_one("0011")) #true
print(dfa_even_zeros_one("011")) #false