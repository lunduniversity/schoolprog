from random import randint

random_number = randint(1, 100)
print("Jag tänker på ett tal mellan 1 och 100")

found = False

while not found:
  guess = int(input("Gissa vilket tal jag tänker på!"))
  if guess == random_number:
    print("Snyggt jobbat! Det var rätt!")
    found = True
  elif guess < random_number:
    print("Tyvärr. Det var för lågt.")
  else:
    print("Tyvärr. Det var för högt.")

print("Jag tänkte på " + str(random_number))
