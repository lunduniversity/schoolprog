from random import randint

max_number = 1000000000
random_number = randint(1, max_number)
print("Slumptalet är: " + str(random_number))

found = False
low = 0
high = max_number+1
tries = 0

while not found:
  guess = low + (high-low)//2
  print("Gissning: " + str(guess))
  tries += 1
  if guess == random_number:
    found = True
  elif guess < random_number:
    low = guess
  else:
    high = guess

print("Det behövdes " + str(tries) + " gissningar")
