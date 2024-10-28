def isValid(s: str) -> bool:
    close_check = [1, 1, 1]
    new_list = list(s)
    for index, c in enumerate(s):
        if c == "(":
            for idx in range(index, len(s)):  # might be weird
                if s[idx] == ")":
                    close_check[0] = 1
                    break
                else:
                    close_check[0] = 0
    for index, c in enumerate(s):
        if c == "{":
            for idx in range(index, len(s)):  # might be weird
                if s[idx] == "}":
                    close_check[1] = 1
                    break
                else:
                    close_check[1] = 0

    for index, c in enumerate(s):
        if c == "[":
            for idx in range(index, len(s)):  # might be weird
                if s[idx] == "]":
                    close_check[2] = 1
                    break
                else:
                    close_check[2] = 0

    if all(value == 1 for value in close_check):
        return True
    else:
        return False

def isValid1(s: str) -> bool:
    stack = []
    for char in s:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            char1 = stack[-1]
            stack.pop()
            if (char == ')' and char1 == '(') or (char == ']' and char1 == '[') or (char == '}' and char1 == '{'):
                continue
            else:
                return False
    return len(stack) == 0

if __name__ == "__main__":
    print(isValid1("()"))