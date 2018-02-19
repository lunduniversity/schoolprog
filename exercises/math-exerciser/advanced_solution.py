from random import randint, choice
from operator import add
from re import search


def process_question(question):
    numbers = []
    regex = r"\{(\d+)-(\d+)\}"
    m = search(regex, question)
    while m:
        n = randint(int(m.group(1)), int(m.group(2)))
        numbers.append(n)
        question = question[:m.start()] + str(n) + question[m.end():]
        m = search(regex, question)

    return question, numbers


questions = [
    ('Vad är "{1-100} + {1-10}"?', add),
    ('Vad är derivatan av "{1-5}x^2 + {1-5}x + {1-10}"?', lambda a2, a1, a0: "{}x + {}".format(a2 * 2, a1)),
]

cont = True
while cont:
    n_correct = 0
    for _ in range(10):
        question, answer_function = choice(questions)
        question, numbers = process_question(question)
        user_answer = input(question + ": ")
        actual_answer = answer_function(*numbers)

        if user_answer == str(actual_answer):
            print("Rätt svar!")
        else:
            print("Tyvärr, rätt svar är {}".format(actual_answer))

    print("Du svarade rätt på {} av 10 frågor.".format(n_correct))
    play_again = input("Vill du spela igen?: ")
    cont = play_again == "ja"
