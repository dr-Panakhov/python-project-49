from random import randint, randrange, choice

beschreibung = 'What is the result of the expression?'


def log_gen_ziffer():
    operation = choice(['+', '-', '*'])
    number1 = randrange(1, 50)
    number2 = randrange(1, 50)
    question = f'{number1}{operation}{number2}'
    if operation == '+':
        correct_answer = number1 + number2
    elif operation == '-':
        correct_answer = number1 - number2
    else:
        correct_answer = number1 * number2
    return question, str(correct_answer)

