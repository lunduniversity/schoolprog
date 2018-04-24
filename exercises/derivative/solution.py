import matplotlib.pyplot as plt

# plotta funktionen f för a <= x <= b
def fplot(f, a, b, lbl):
	N = 1000             # Antalet punkter att plotta
	dx = (b - a) / (N-1) # Avståndet mellan punkterna
	xs = [a + i*dx for i in range(N)]
	ys = [f(a + i*dx) for i in range(N)]
	plt.plot(xs, ys, label=lbl)

import math

# ------------------------------------------------
# 1-3

def g(x):
  return math.exp(-0.1*x) * math.cos(x)

def gderiv(x):
  h = 0.00001
  return (g(x+h) - g(x)) / h

fplot(g, 0, 10, "g")
fplot(gderiv, 0, 10, "g'")

plt.title("g och gderiv")
plt.legend(loc = "upper center")
plt.grid(True)
plt.savefig('plot1.png')

# ------------------------------------------------
# 4

def s1(x):
  return math.exp(-0.1*x) * math.cos(x) - 0.1*math.exp(-0.1*x) * math.sin(x)

def s2(x):
  return -0.1 * math.exp(-0.1*x) * math.cos(x) - math.exp(-0.1*x) * math.sin(x)

def s3(x):
  return -0.1 * math.exp(-0.1*x) * math.cos(x) - 0.1*math.exp(-0.1*x) * math.sin(x)

def diff1(x):
  return gderiv(x) - s1(x)

def diff2(x):
  return gderiv(x) - s2(x)

def diff3(x):
  return gderiv(x) - s3(x)

plt.clf()   # töm grafen
plt.title("tre vänner deriverar")

fplot(diff1, 0, 10, "g' - s1")
fplot(diff2, 0, 10, "g' - s2")
fplot(diff3, 0, 10, "g' - s3")

plt.legend(loc = "upper center")
plt.grid(True)
plt.savefig('plot2.png')

# ------------------------------------------------
# 5-6

def deriv(f, x):
  h = 0.00001
  return (f(x+h) - f(x)) / h

plt.clf()   # töm grafen
plt.title("derivering med lambdauttryck")

fplot(g, 0, 10, "g")
fplot(lambda x: deriv(g, x), 0, 10, "g'")

plt.legend(loc = "upper center")
plt.grid(True)
plt.savefig('plot3.png')

# ------------------------------------------------
# 7

plt.clf()   # töm grafen
plt.title("några derivator")

fplot(math.sin, -1, 1, "abs")
fplot(lambda x: deriv(math.sin, x), -1, 1, "sin'")

fplot(abs, -1, 1, "abs")
fplot(lambda x: deriv(abs, x), -1, 1, "abs'")

fplot(math.log, 0.1, 1, "log")
fplot(lambda x: deriv(math.log, x), 0.1, 1, "log'")

plt.legend(loc = "upper center")
plt.grid(True)
plt.savefig('plot4.png')
