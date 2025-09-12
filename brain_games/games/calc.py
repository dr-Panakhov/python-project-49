from random import randint, choice

description = 'What is the result of the expression?'

start_n = 1
stop_n= 50

def log_gen_ziffer():
    operation = choice(['+', '-', '*']) #NOSONAR
    number1 = randint(start_n, stop_n) #NOSONAR
    number2 = randint(start_n, stop_n) #NOSONAR
    question = f'{number1} {operation} {number2}' #NOSONAR
    if operation == '+':
        correct_answer = number1 + number2
    elif operation == '-':
        correct_answer = number1 - number2
    elif operation == '*':
        correct_answer = number1 * number2
    return question, str(correct_answer)

