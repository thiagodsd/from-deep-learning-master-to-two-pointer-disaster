"""
psychological support
    [42]
    []
    [14]
    "14"
    []
"""

input()
queries = list()

while True:
    try:
        queries.append(input().rstrip())
    except:
        break    
        
stack = list()
tail = 0
for q in queries:
    q_id, *val = q.split()
    if q_id == "1":
        stack.append(val[0])
    elif q_id == "2":
        tail += 1
    elif q_id == "3":
        print(stack[tail])
