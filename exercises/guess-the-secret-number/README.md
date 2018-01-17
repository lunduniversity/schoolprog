Guess the secret number
======================

Write a program that randomizes a number and lets you guess which number it is.

The process will go something like this:

 1. Randomize a number; In order to make python give you a random number you will have to first import the method randint() from a package called random. You can do this by copying the following code to the editor:
 ```python
 from random import randint

 # Generates a number between 0 and 10 and assigns it to "random_number". "Random_number" will be the variable you will be using, a mystery number.
 random_number = randint(0, 10)
```


 2. Now you want code for asking the user to guess the number. Copy the following code to the editor:
 ```python
 # Reads a line of input and converts it to an integer, then assigns this number to "guessed_number".
 guessed_number = int(input("Write something here!"))
 ```
 3. You want to be able to keep guessing as long as guessed_number isn't the same value as random_number. In order to do this you can use        something called a while-loop. Check this following example and try to figure out how you can use it for your own program:
 ```python
 a = 10
 b = 13
 
 # This line of code under the while-block will keep repeating it self untill the condition is no longer fullfilled. Since 10 is not 13 the code will repeat itself.
 while a is not b:
  b = int(input("Assign a new value to b with new input))
 ```
 4. Now, it is still difficult to just randomly keep guessing numbers. Depending on the intervall it can take a great amount of time. You can make it easier if you can hint on wether to guess higher or lower when comparing to random_number. To do this you can use an if-statement within your while-loop. Check these following exampels:
  ```python
 a = 10
 b = 13
 
 while a != b:
 
  if a < b:
   b = int(input("Try a lower number!))
  
  if a > b:
   b = int(input("Try a higher number!))
 ```
 
 4. Some feedback to when you actually guessed the right number, for that you want to add after the while-loop a line of code that just prints out a string of text. You can try this command for that purpose:
   ```python
   print("Here you can write whatever you want and it will show in the terminal!")
   ```
  
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
elif a != 10:
    print("a is not equal to 10")
else:
    print("a is larger than 10")
```


### Repetition

Repeat an action while a statement is true

```python
while a < 10:
    print("a is less than 10")
```



