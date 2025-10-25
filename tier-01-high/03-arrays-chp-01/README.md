# tl;dr

the way to reduce $O(n^2)$ to $O(n)$ with two pointers

## mental triggers

- ordered array & search for pair/triplet? -> two pointers
- need to traverse from both ends? -> left/right pointers
- fixed sliding window? -> two pointers

## common anti-patterns

```python
# ❌ DON'T: O(n**2) when array is already sorted
for i in range(len(arr)):
    for j in range(i+1, len(arr)):  # wastes sorting
```

## the correct pattern

```python
left, right = 0, len(arr) - 1
while left < right:
    current = arr[left] + arr[right]
    if current == target:
        return [left, right]
    elif current < target:
        left += 1
    else:
        right -= 1
```

## problems

`TODO`