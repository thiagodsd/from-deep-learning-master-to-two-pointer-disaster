# tl;dr

manipulating & frequency counting

## mental triggers

- strings are just arrays of chars -> same array patterns apply
- anagram/permutation? -> count characters with dict
- substring? -> sliding window

## common anti-patterns

```python
# same as arrays
```

## the correct pattern

```python
# anagram check
from collections import Counter
Counter(s1) == Counter(s2) # Counter('abcde') -> {'a':1, 'b':1, 'c':1, 'd':1, 'e':1}

# character frequency
char_count = dict()
for char in s:
    char_count[char] = char_count.get(char, 0) + 1
```

## problems

`TODO`

<br/><br/><br/><br/><br/>

# tl;dr

sliding window in arrays/strings

## mental triggers

- continuous subarray/substring with condition? -> sliding window
- 'longest/shortest satisfying X'? -> expandable window
- fixed-size window? -> two pointers is better

## common anti-patterns

```python
# ❌ DON'T: to recompute entire window at each step
for i in range(len(arr)):
    for j in range(i, len(arr)):
        window = arr[i:j+1]  # O(n**3) with slicing
```

## the correct pattern

```python
left = 0
for right in range(len(arr)):
    # add arr[right] to the window
    while window_invalid():
        # remove arr[left] from the window
        left += 1
    # update result
```

## problems

`TODO`
