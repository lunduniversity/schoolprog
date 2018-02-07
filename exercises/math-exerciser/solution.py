from random import randint

min_number = 0
max_number = 10

questions = []
for i in range(min_number, max_number):
    for j in range(min_number, max_number):
        questions.add(('Vad är "{} * {}"?', i + j))
        questions.add(('Vad är "{} + {}"?', i + j))
        questions.add(('Vad är "{} - {}"?', i - j))

question_index = randint(0, len(questions) - 1)
selected_question = questions[question_index]
number1 = randint(min_number, max_number)
number2 = randint(min_number, max_number)

user_answer = input(selected_question[0].format(number1, number2) + ": ")
actual_answer = selected_question[1](number1, number2)

if user_answer == str(actual_answer):
    print("Rätt svar!")
else:
    print("Tyvärr, rätt svar är {}".format(actual_answer))
