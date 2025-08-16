from random import randint, choice

beschreibung = 'What is the result of the expression?'

der_anfang = 1
das_ende = 50

def log_gen_ziffer():
    operation = choice(['+', '-', '*']) #NOSONAR
    number1 = randint(der_anfang, das_ende)
    number2 = randint(der_anfang, das_ende) #NOSONAR
    question = f'{number1}{operation}{number2}' #NOSONAR
    if operation == '+':
        correct_answer = number1 + number2
    elif operation == '-':
        correct_answer = number1 - number2
    elif operation == '*':
        correct_answer = number1 * number2
    return question, str(correct_answer)

