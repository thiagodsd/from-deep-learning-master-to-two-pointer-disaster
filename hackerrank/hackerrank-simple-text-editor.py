# following the naming convetion
stack = list()
for i in range(int(input().rstrip())):
    operation, *query = input().rstrip().split()
    if operation == "1":
        stack.append(stack[-1] + query[0] if stack else query[0])
    if operation == "2":
        current = stack[-1]
        stack.append(current[: len(current) - int(query[0])])
    if operation == "3":
        print(stack[-1][int(query[0]) - 1])
    if operation == "4":
        stack.pop()
