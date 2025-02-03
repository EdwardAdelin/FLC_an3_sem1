def q0(char):
    if char == '0':
        return q1
    return reject

def q1(char):
    if char == '0':
        return q2
    return reject

def q2(char):
    if char == '0':
        return q1
    if char == '1':
        return q3
    return reject

def q3(char):
    if char == '1':
        return q3
    return reject

def reject(char):
    return reject

def is_in_language(word):
    state = q0
    for char in word:
        state = state(char)
    return state == q3

print(is_in_language("001"))  # t
print(is_in_language("00"))  # f




