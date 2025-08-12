from random import randint, choice

beschreibung = 'What is the result of the expression?'


def log_gen_ziffer():
    operation = choice(['+', '-', '*'])
    number1 = randint(1, 15)
    number2 = randint(1, 15)
    question = f'{number1}{operation}{number2}'
    if operation == '+':
        correct_answer = number1 + number2
    elif operation == '-':
        correct_answer = number1 - number2
    elif operation == '*':
        correct_answer = number1 * number2
    return question, str(correct_answer)

