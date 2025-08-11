import random

beschreibung = 'What is the result of the expression?'


def log_gen_ziffer():
    operation = random.choice(['+', '-', '*'])
    ziffer_1 = random.randrange(1, 50)
    ziffer_2 = random.randrange(1, 50)
    result = f'{ziffer_1}{operation}{ziffer_2}'
    if operation == '+':
        richtige_anwort = ziffer_1 + ziffer_2
    elif operation == '-':
        richtige_anwort = ziffer_1 - ziffer_2
    else:
        richtige_anwort = ziffer_1 * ziffer_2
    return result, str(richtige_anwort)

