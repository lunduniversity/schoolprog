Implement Arithmetic Operators
==============================

 - Option: Implement an addition function using just the `-` operator.
 - Implement a function multiply using just a for loop and the previously implemented add function (or the `+` operator).
 - Using your multiply function, implement a power function.

## Code

```python
def add(a, b):
    return a - (-b)

def mul(a, b):
    acc = 0
    for i in range(b):
        acc = add(acc, a)
    return acc

def power(a, b):
    acc = 1
    for i in range(b):
        acc = mul(acc, a)
    return acc
```

