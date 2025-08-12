import random

beschreibung = 'What is the result of the expression?'


def log_gen_ziffer():
    operation = random.choice(['+', '-', '*'])
    number1 = random.randrange(1, 50)
    number2 = random.randrange(1, 50)
    question = f'{number1}{operation}{number2}'
    if operation == '+':
        correct_answer = number1 + number2
    elif operation == '-':
        correct_answer = number1 - number2
    else:
        correct_answer = number1 * number2
    return question, str(correct_answer)

