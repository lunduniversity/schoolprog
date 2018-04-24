import matplotlib.pyplot as plt

# plotta funktionen f för a <= x <= b
def fplot(f, a, b, lbl):
	N = 1000             # Antalet punkter att plotta
	dx = (b - a) / (N-1) # Avståndet mellan punkterna
	xs = [a + i*dx for i in range(N)]
	ys = [f(a + i*dx) for i in range(N)]
	plt.plot(xs, ys, label=lbl)

import math

def g(x):
  return math.exp(-0.1*x) * math.cos(x)

h = 0.00001

def gderiv(x):
  return (g(x+h) - g(x)) / h

def deriv(f, x):
	return (f(x+h) - f(x)) / h

fplot(g, 0, 10)
fplot(gderiv, 0, 10)

def s1(x):
  return math.exp(-0.1*x) * math.cos(x) - 0.1*math.exp(-0.1*x) * math.sin(x)

def s2(x):
  return -0.1 * math.exp(-0.1*x) * math.cos(x) - math.exp(-0.1*x) * math.sin(x)

def s3(x):
  return -0.1 * math.exp(-0.1*x) * math.cos(x) - 0.1*math.exp(-0.1*x) * math.sin(x)

def diff1(x):
  return deriv(x) - s1(x)

def diff2(x):
  return deriv(x) - s2(x)

def diff3(x):
  return deriv(x) - s3(x)

# fplot(diff1, 0, 10)
fplot(diff2, 0, 10)
# fplot(diff3, 0, 10)

# spara grafen i en png-fil
plt.savefig('plot.png')
