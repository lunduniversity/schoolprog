---
title: Calculating and comparing interest rates
layout: page
toc: true
type: exercise
permalink: /exercises/interest-rates/
---

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
Start of by reading the part about functions in the [cheatsheet](../../cheatsheet/python/), below you will
find another example of a function. The function below converts a given time
of hours (h) into the time minutes (m):

```python
def minute_converter(h):
    m = h * 60
    return m
```
"return" will give back a value when calling the
function, here we will get "m", the minutes.

##  Part B

Now try running the program you wrote in Part A. You will have to call your
function last, that is after you have declared your function.

The following sample describes how a function is first declared and then
called:

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

Now try to run your new program!
