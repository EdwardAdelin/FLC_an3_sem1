def state_q0(word):
    if not word:
        return False
    if word[0] == '1':
        return state_q1(word[1:])
    return False

def state_q1(word):
    if not word:
        return True
    if word[0] == '1':
        return state_q1(word[1:])
    return False

def is_in_language(word):
    return state_q0(word)

print(is_in_language("111"))  # t
print(is_in_language("11a1"))  # f