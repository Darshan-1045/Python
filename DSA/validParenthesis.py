input = "{[)]}"

stack = []

start = "{[("

for char in input:

    if char in start:
        stack.append(char)

    else:
        if not stack:
            print("Invalid parenthesis")
            break

        if (char == "}" and stack[-1] == "{") or \
           (char == "]" and stack[-1] == "[") or \
           (char == ")" and stack[-1] == "("):

            stack.pop()

        else:
            print("Invalid parenthesis")
            break

else:
    if not stack:
        print("Valid parenthesis")
    else:
        print("Invalid parenthesis")