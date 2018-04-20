# ----------------------------------
import matplotlib.pyplot as plt

legends=[]

# plotta funktionen f för a <= x < b
def fplot(f, a, b, lbl):
  global legends
  N = 1000
  dx = (b - a) / N
  xs = [a + i*dx for i in range(N)]
  plothandle = plt.plot(xs, list(map(f, xs)), label=lbl)
  legends.append(plothandle[0])
# ----------------------------------

import math

def g(x):
  return math.exp(-0.1*x) * math.cos(x)

h = 0.00001
def deriv(x):
  return (g(x+h) - g(x)) / h

fplot(g, 0, 10, 'g')
fplot(deriv, 0, 10, 'deriv')

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

fplot(diff1, 0, 10, 'diff1')
fplot(diff2, 0, 10, 'diff2')
fplot(diff3, 0, 10, 'diff3')

# spara grafen i en png-fil
plt.legend(handles=legends)
plt.savefig('plot.png')
