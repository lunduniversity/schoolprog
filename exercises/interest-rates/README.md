#   Calculating and comparing interest rates

In this exercise you will learn the basic concept of functions in Python. You
will create your own function and then call it from antother function.  

##  Part A

Your assignment is to create method which allows you to calculate the total
amount on your account after a certain amount of time and with a specified rate. You will have three different
variables to work with:
    Time t
    Rate r
    Starting Amount s

### Functions in Python
Here is an example of a function in python that converts the time in hours (h)
into the time minutes (m):

```python
def minute_converter(h):
    m = h * 60
    return m
```

"def" is common keyword reserved in Python that tells the compiler that the
code that follows is a function. The following code is the name of the
function, usually with small letters and "_" between words. Pick a self
explanatory name for your own sake, it will be easier to remember. Inside the
parentheses is where you can put parameters, potential input for your function (here we
have h for the hours that are going to be converted). Also here you should
think about self explanatory variable names. After the parentheses is a ":",
this will tell the compilator where the block of code starts fot the function.
Indentation (the extra space before the code) will then tell the compilator
what is part of the function. "return" will give back a valuw when calling the
function, here we will get "m", the minutes.

##  Part B

Now try running the program you wrote in Part A. You will have to call your
function last, that is after you have declared your function.

### Running a function in Python

```python
def minute_converter(h):
    m = h * 60
    return m

minute_converter(2)
```

When we call this function in Python with the input "2" we will get 120 in
return (2*60).

##  Part C

It is much more interesting to compare which banks are the most adventagous
for saving money. For this purpose you want to create a new function that uses
the function previous part of the assignment. You want the function to
compare two banks and return which bank that helps you save the most
amount of money. In this case you also want to examine the different
yearly costs you will have to pay as a customer from a certain bank. You
will have even more parameters for your function this time, both banks
information and also both banks indiviudal costs.

```python
def minute_compare(h1, h2):
    m1 = minute_converter(h1)
    m2 = minute_converter(h2)
    if(m1 > m2):
        return m1
    else:
        return m2
```
##   Part D

Now try your new program in the compilator!
