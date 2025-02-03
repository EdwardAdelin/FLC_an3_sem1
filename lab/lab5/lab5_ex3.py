def q0(char):
    global first_letter
    first_letter = char
    return q1

def q1(char):
    if char == first_letter:
        return q_accept
    return q1  

def q_accept(char):
    return q_accept

def reject(char):
    return reject


def is_in_language(word):
    global first_letter
    first_letter = None
    state = q0  
    for i, char in enumerate(word):
        if i == len(word) - 1:
            state = state(char)
        else:
            state = state(char)
    return state == q_accept

print(is_in_language("abca"))  #t
print(is_in_language("python"))  # f