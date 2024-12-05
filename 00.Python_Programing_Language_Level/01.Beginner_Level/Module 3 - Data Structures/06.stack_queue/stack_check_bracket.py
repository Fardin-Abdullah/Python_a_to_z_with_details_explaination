def is_balanced(input_str):
    s = list()
    matching_bracket = {')': '(', ']': '[', '}': '{'}
    
    for ch in input_str:
        if ch in "({[":
            s.append(ch)
        elif ch in ")}]":
            if not s or s[-1] != matching_bracket[ch]:
                return False
            s.pop()

    return not s

if __name__ == "__main__":
    input_str = input("Enter here: ")
    if is_balanced(input_str):
        print(input_str, "is balanced.")
    else:
        print(input_str, "is not balanced.")

def is_balanced(input_str):
    s = list()
    matching_bracket = {')': '(', ']': '[', '}': '{'}
    
    for ch in input_str:
        if ch in "({[":
            s.append(ch)
        elif ch in ")}]":
            if not s or s[-1] != matching_bracket[ch]:
                return False
            s.pop()

    return not s

if __name__ == "__main__":
    input_str = input("Enter here: ")
    if is_balanced(input_str):
        print(input_str, "is balanced.")
    else:
        print(input_str, "is not balanced.")
