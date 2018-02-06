from random import randint
from operator import add

min_number = 0
max_number = 10
questions = [('Vad är "{} + {}"?', add)]

selected_question = questions[randint(0, len(questions) - 1)]
number1 = randint(min_number, max_number)
number2 = randint(min_number, max_number)

user_answer = input(selected_question[0].format(number1, number2) + ": ")
actual_answer = selected_question[1](number1, number2)

if user_answer == str(actual_answer):
    print("Rätt svar!")
else:
    print("Tyvärr, rätt svar är {}".format(actual_answer))
