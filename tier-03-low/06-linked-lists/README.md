# tl;dr

pointer manipulation

## mental triggers

- it is not usual in data science interviews but if needed -> dummy node solves many problems

## common anti-patterns

```python
# TODO
```

## the correct pattern

```python
dummy = ListNode(0)
dummy.next = head
current = dummy
while current.next:
    # manipulate current.next
    current = current.next
return dummy.next
```

## problems

`TODO`

