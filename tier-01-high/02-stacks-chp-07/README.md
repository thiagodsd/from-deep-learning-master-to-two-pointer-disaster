# tl;dr

lifo (last in, first out) data structure for managing nested structures and backtracking

## mental triggers

- is there any pair/parenthesis matching? -> stack
- is there any backward navigation (undo/back)? -> stack
- do i need to process "inside out"? -> stack

## common anti-patterns

```python
# ❌ DON'T: to use list and manual indexing
opened = list()
closed = list()
# it is error prone and hard to read
```

## the correct pattern

```python
stack = list()
for char in sequence:
    if is_opening(char):
        stack.append(char)  # push
    else:
        if not stack or not matches(stack[-1], char):
            return False
        stack.pop()  # pop
return len(stack) == 0
```

## problems

`TODO`