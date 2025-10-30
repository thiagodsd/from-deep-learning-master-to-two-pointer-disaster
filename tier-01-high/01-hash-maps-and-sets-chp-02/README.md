# tl;dr

the way to avoid $O(n^2)$ nested loops is to use hash maps and sets for $O(1)$ lookups

## mental triggers

- do i need to count/search for things repeatedly?
  - nested loops -> $O(n^2)$ fail
  - hash maps/sets -> $O(1)$ win

## common anti-patterns

```python
# ❌ DON'T: nested loop
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] + arr[j] == target:  # O(n**2)
```

## the correct pattern

```python
# frequency counter
freq = dict()
for item in items:
    freq[item] = freq.get(item, 0) + 1

# existence check
seen = set(items)
if target in seen:  # O(1)
```

## problems

- [LeetCode: Two Sum](https://leetcode.com/problems/two-sum/) or [HackerRank: Pair Sums](https://www.hackerrank.com/contests/hourrank-26/challenges/pair-sums/problem)
- [HackerRank: Check Magazine (Ransom Note)](https://www.hackerrank.com/challenges/ctci-ransom-note/problem)
- [HackerRank: Ice Cream Parlor](https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem)
- [HackerRank: Frequency Queries](https://www.hackerrank.com/challenges/frequency-queries/problem)