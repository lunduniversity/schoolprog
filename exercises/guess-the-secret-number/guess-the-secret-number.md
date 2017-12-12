Guess the secret number
======================

Write a program that randomizes a number and lets you guess which number it is.

The process will go something like this:

 1. Randomize a number 
 ```python
 from random import randint

 #Generates a number between 0 and 10
 random_number = randint(0, 10)
```

 2. Ask the user to guess the number
 ```python
 #Read a line of input and converts it to an integer
 guessed_number = int(input())
 ```

 3. Print "Correct!" and exit if the number is correct, otherwise print "lower" or "higher" depending on if the guess is too high or too low. Then go back to step 2.

 *Hint: Use a while loop for step 2 and 3*

## Extra

Write a program that based on a given number and the interval 0 - 100 finds the optimal amount of steps using binary search. 

Example:
```
IN      >>> 10
OUT     6

IN      >>> 50
OUT     1
```

*Binary search:*
https://www.tutorialspoint.com/data_structures_algorithms/binary_search_algorithm



## Cheatsheet

### Variables and printing

```python
x = 10    # the variable x gets the value 10
print(x)  # prints 10
x = "hej" # x value is changed to "hej"
print(x)  # prints "hej"
```

### Kinds of variables
Strings, Integers, Floating Points, Booleans

The kind of a variable is determined when a variable is assigned a value

```python
a = 1        # a is now an integer with the value 1
b = True     # b is now an boolean with the value True
c = False    # c is now an boolean with the value False
d = "1"      # d is now a string with the value "1"
```

### Input

Read a line of input and print the result:

```python
print("What is your name?")
name = input("Name: ")
print("Hello, " + name + "!")
```

### Arithmetic

```python
x0 = 1 + 1  # x0 == 2
x1 = 1 - 1  # x1 == 0
x2 = 2 * 3  # x2 == 6
```

### Control flow

Do different things dependent on expression values:

```python
if a < 10:
    print("a is less than 10")
elif a == 10:
    print("a is equal to 10")
else:
    print("a is larger than 10")
```


### Repetition

Repeat an action while a statement is true

```python
while a < 10:
    print("a is less than 10")
```



