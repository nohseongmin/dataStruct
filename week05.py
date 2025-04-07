#print(1+3))
def is_valid_parentheses(expression : str) -> bool: #type hint 사용(강제아님)
    stack = list()
    for letter in expression:
        #기본 아이디어:(에서 push )에서 pop.
        if letter == "(":
            stack.append(letter)
        if letter == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0

print(is_valid_parentheses(")(1+2))")) #예상) f
print(is_valid_parentheses("(1+2))")) # f
print(is_valid_parentheses("(1+2)")) #t
print(is_valid_parentheses("((3*2)/+2)")) #t

