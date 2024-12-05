def is_balanced(input_str):
    s = list()

    for ch in input_str:
        if ch == "(":
            s.append(ch)
        elif ch == ")":
            if not s:
                return False
            s.pop()

    return not s

if __name__ == "__main__":
    input_str = input("Enter here: ")
    if is_balanced(input_str):
        print(input_str, "is balanced.")
    else:
        print(input_str, "is not balanced.")
