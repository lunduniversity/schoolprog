from random import randint

min_number = 0
max_number = 10

questions = []
answers = []
for i in range(min_number, max_number):
    for j in range(min_number, max_number):
        question = 'Vad är {} * {}?'.format(i, j)
        answer = i * j
        questions.append(question)
        answers.append(answer)

        question = 'Vad är {} + {}?'.format(i, j)
        answer = i + j
        questions.append(question)
        answers.append(answer)

        question = 'Vad är {} - {}?'.format(i, j)
        answer = i - j
        questions.append(question)
        answers.append(answer)


question_index = randint(0, len(questions) - 1)
selected_question = questions[question_index]
actual_answer = answers[question_index]

user_answer = input(selected_question + ": ")

if user_answer == str(actual_answer):
    print("Rätt svar!")
else:
    print("Tyvärr, rätt svar är {}".format(actual_answer))
