# 1. Addition och negation

print("Addition och negation:")

def add(a, b):
  return a + b

def neg(a):
  return -a

# Undersök uttryck
print(add(3, 5))
print(neg(7))
print(add(add(3, 5), neg(7)))
print(add(neg(7), add(3, 5)))

# Använd add, neg, 2, 5, 10

# 4
print(add(2, 2))

# 7
print(add(2, 5))

# 8
print(add(10, neg(2)))
# eller
print(add(add(2, 2), add(2, 2)))
# eller på andra sätt

# Tre olika sätt att skriva 6
print(add(add(2, 2), 2))
print(add(10, neg(add(2, 2))))
print(add(add(5, neg(2)), add(5, neg(2))))
# eller på andra sätt

# 2. Subtraktion

print("Subtraktion:")

def sub(a, b):
  return add(a, neg(b))

print(sub(100, 3))
print(sub(1, 1001))

print(add(sub(5, 2), sub(10, 2)))

# 3. Multiplikation

print("Multiplikation:")

def mul(a, b):
  result = 0
  for i in range(b):
    result = add(result, a)
  return result

print(mul(3, 5))
print(mul(0, 10))
print(mul(1000, 1000))

# 4. Heltalsdivision

print("Heltalsdivision:")

def intdiv(a, b):
  length = 0
  bricks = 0
  while (length <= a):
    length = add(length, b)
    bricks = add(bricks, 1)
  return sub(bricks, 1)

print(intdiv(14, 3))
print(intdiv(12, 4))

# 5. Exponentiering

print("Exponentiering:")

def power(b, n):
  result = 1
  for i in range(n):
    result = mul(result, b)
  return result

print(power(3, 5))
print(power(137, 0))
