# tl;dr

dynamic programming = recursion + memoization (caching) to avoid redundant work

## mental triggers

- how many ways to...
- min/max cost to...
- longest/shortest...
- i'm solving the same subproblem multiple times
    - recursion without memoization -> exponential time (DON'T)
    - recursion with memoization -> polynomial time (DO)

## common anti-patterns

```python
# ❌ DON'T: naive recursion (exponential time)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2) # O(2**n)
```

## the correct pattern

### top-down (memoization)

```python
# save results of subproblems in a dictionary
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)  # O(n)
    return memo[n]
```

### bottom-up (tabulation)

```python

def fib(n):
    dp = [0] * (n + 1)
    dp[0] = base_value
    dp[1] = base_value
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]  # O(n)
```

## problems

`TODO`
