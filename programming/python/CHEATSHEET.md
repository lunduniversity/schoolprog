---
title: Cheatsheet
layout: page
toc: true
permalink: /cheatsheet/python/
---

## Variables and printing

```python
x = 10    # the variable x gets the value 10
print(x)  # prints 10
x = "hej" # x value is changed to "hej"
print(x)  # prints "hej"
```

## Kinds of variables
Strings, Integers, Floating Points

The kind of a variable is determined when a variable is assigned a value

```python
a = 1        # a is now an integer with the value 1
a = "1"      # a is now a string with the value "1"
a = int("1") # "1" is converted to the integer 1
a = str(1)   # 1 is converted to the string "1"
a = float(1) # 1 is converted to the float 1.0
a = 1/1      # 1/1 evaluates to the float 1.0
```

Note that ``` int("hej") ``` will crash on evaluation. 
The ```int``` and ```float``` functions expects values that can be interpreted as numbers.

## Arithmetic

```python
x0 = 1 + 1  # x0 == 2
x1 = 1 - 1  # x1 == 0
x2 = 2 * 3  # x2 == 6
x3 = 3 / 2  # x3 == 1.5
x4 = 3 // 2 # x4 == 1, largest integer <= 3/2
x5 = 3 % 2  # x5 == 1, 3 mod 2 == 1
x6 = 2 ** 3 # x6 == 8, (2^3).
```
Lots of mathematical functions, like ```sin``` and ```sqrt``` are avaliable in the ```math``` package.
```python
import math
print(math.sqrt(4)) # prints 2
```

## Control flow

Do different things dependent on expression values:

```python
if a < 10:
    print("a is less than 10")
elif a == 10:
    print("a is equal to 10")
else:
    print("a is larger than 10")
```

## Iteration

Print the first 10 powers of 2:

```python
for i in range(10):
    print(i**2)
```

Iterate over the first 10 natural numbers and print the odd ones:
```python 
for i in range(10):
    if i%2 == 1:
        print(i)
```

## Input

Read a line of input and print the result:

```python
print("What is your name?")
name = input("Name: ")
print("Hello, " + name + "!")
```

Read a whole number from input:

```python
n = int(input())  # The number given by
for i in range(n):
    print(i * 2)
```


## Functions

Calculate the hypotenuse of a right-angled triangle with two decimal numbers as input:

```python
base = float(input("Base: "))  # Can be a number with decimals (a "floating point number")
side = float(input("Side: "))
hypotenuse = sqrt(base**2 + side**2)
print("The hypotenuse is: " + str(hypotenuse))  # You must convert the number to a string before adding to another string
```

If we want to compute this many times in our code, we can define a function instead:

```python
from math import sqrt

def hypotenuse(base, side):
    return sqrt(base**2 + side**2)

print(hypotenuse(1, 1)) # prints 1.4142135623730951
print(hypotenuse(3, 4)) # prints 5.0 
```

A function definition in python starts with ```def```, then follows the name and an argument list, possbibly empty.
Then follows some python code, and it ends with ```return x``` where x is an expression.

## Lists

Build a simple list:

```python
l = [1, 2, 3]
print(l)
```

Do something to each number in a list:

```python
l = [1, 2, 3]
for number in l:
    print(number * 2)
```

Build a list with the first `n` whole numbers and sum them together:

```python
n = 100
l = list(range(n))
print(sum(l))
```


## Debugging

Ensure that a statement is true, otherwise crash.

```python
assert True        # Will work fine
assert 3 * 2 == 6  # Will work fine
assert 1 + 1 == 3  # Will crash the program
```
