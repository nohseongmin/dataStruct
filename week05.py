def is_valid(expression : str) -> bool:
    brachets = {')': '(', ']': '[', '}': "{"}
    stack = list()
    for letter in expression:
        if letter in brachets.values():
            stack.append(letter)
        if letter in brachets.keys():
            if not stack or stack.pop() != brachets[letter]:
                return False
    return not stack

print(is_valid("[1+2]+(1+2)"))
print(is_valid("[1+2]+1+2)"))
print(is_valid("[1+2]+1+2"))
print(is_valid("{([1+2])}"))
print(is_valid("({[1+2])}"))


