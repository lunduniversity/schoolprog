Cheatsheet for Python
=====================

Add two numbers together and print the result:

```python
print(1+2)
```

## Control flow

TODO

## Iteration

Print the power 2 of the first 10 whole numbers:

```python
for i in range(10):
    print(i**2)
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
n = int(input())  # Can only be a whole number (an "integer")
for i in range(n):
    print(i * 2)
```

Calculate the hypotenuse of a right-angled triangle with two decimal numbers as input:

```python
base = float(input("Base: "))  # Can be a number with decimals (a "floating point number")
side = float(input("Side: "))
hypotenuse = sqrt(base**2 + side**2)
print("The hypotenuse is: " + str(hypotenuse))  # You must convert the number to a string before adding to another string
```

## Debugging

Ensure that a statement is true, otherwise crash.

```python
assert True        # Will work fine
assert 3 * 2 == 6  # Will work fine
assert 1 + 1 == 3  # Will crash the program
```
