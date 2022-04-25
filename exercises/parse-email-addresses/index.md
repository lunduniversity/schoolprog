Parse email addresses
======================

You have been given a list of email addresses that you want to send an emails to.

However, these email addresses seems to have been taken somewhere from the internet. On the internet it is pretty common that dots are replaced by [dot] and ats are replaced by [at]. You'd like to have a program that converts these email addresses into valid ones.

Write a function parse\_simple that given an email address, replaces "[at]"with "@" - if there is one, and replaces all occurences of "[dot]" with ".".

```python
def parse_simple(email): ???

assert parse_simple("a[dot]b[at]gmail[dot]com") == "a.b@gmail.com"
assert parse_simple("a.b[at]gmail[dot]com") == "a.b@gmail.com"
assert parse_simple("a[dot]b@gmail[dot]com") == "a.b@gmail.com"
assert parse_simple("[at][at][at][at]") == "@@@@"
assert parse_simple("[dot][at][dot][at]") == ".@.@"
```

Write a program (script) that for each line l in the input, prints parse_simple(l).

## Todo:
- More complicated replacement rules, where [dot] is [punkt], etc.
- Function that checks if an email address is correctly formated, something like: {text}@{text}.{text}, with some more restrictions, only dots allowed in first text, etc.
- What to do with email addresses that does not match?
    + Keep
    + Discard
    + Interactive (Let the user choose. Need to not read the emails from stdIn in that case.)
