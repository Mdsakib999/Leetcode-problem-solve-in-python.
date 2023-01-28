def isValid(s: str) -> bool:
    left_symb = []

    for chr in s:
        if chr in ['(', '{', '[']:
            left_symb.append(chr)

        elif chr == ")" and len(left_symb) != 0 and left_symb[-1] == "(":
            left_symb.pop()

        elif chr == '}' and len(left_symb) != 0 and left_symb[-1] == '{':
            left_symb.pop()
        elif chr == ']' and len(left_symb) != 0 and left_symb[-1] == '[':
            left_symb.pop()

        else:
            return False

    return left_symb == []

given_string = input("Enter string: ") #take input from usear

print(isValid(given_string))

#print(isValid("(){}"))