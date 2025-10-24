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