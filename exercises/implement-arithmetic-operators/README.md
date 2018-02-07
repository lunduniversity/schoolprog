---
title: Implementera aritmetiska operatorer
toc: true
layout: page
type: exercise
tags:
 - aritmetik
 - funktioner
permalink: /exercises/implement-arithmetic-operators/
---

 - Implement the arithmetic functions (subtract, mul, floordiv) using only an add function and a negate function.
    - Implement subtraction by using add and negation in the correct order.
    - Implement a function multiply using just a for loop and the add function.
    - Implement integer division by searching over the answer.
 - Using your multiply function, implement a power function.

```python
def add(a, b):
    return a + b

def neg(a):
    return -a
```

```python
def sub(a, b): ???
def mul(a, b): ???
def div(a, b): ???
```

## Code

```python
def sub(a, b):
    return add(a, neg(b))

def mul(a, b):
    acc = 0
    for i in range(b):
        acc = add(acc, a)
    return acc

def div(a, b):
    for i in range(a):
        if mul(i, b) > a:
            return sub(i, 1)

def power(a, b):
    acc = 1
    for i in range(b):
        acc = mul(acc, a)
    return acc
```

