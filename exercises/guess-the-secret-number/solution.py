from random import randint

min_number = 0
max_number = 100

random_number = randint(min_number, max_number)

found = False

while not found:
    guess = int(input())
    if guess is random_number:
        print('Correct!')
        found = True
    elif guess < random_number:
        print('higher')
    elif guess > random_number:
        print('lower')


