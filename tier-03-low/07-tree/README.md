# tl;dr

recursive bfs (breadth-first search) or dfs (depth-first search) traversal of tree structures

## mental triggers

- hierarchical data? -> tree
- level-order? -> bfs (queue)
- any other thing? -> dfs (recursion/stack)

## common anti-patterns

```python
# TODO
```

## the correct pattern

```python
# most common: dfs
def dfs(node):
    if not node:
        return
    # process node
    dfs(node.left)
    dfs(node.right)
```

## problems

`TODO`

