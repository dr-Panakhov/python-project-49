import random
from prompt import string
def log_gen_ziffer(operation):
    ziffer_1 = random.randrange(1,50)
    ziffer_2 = random.randrange(1,50)
    result = f'{ziffer_1}{operation}{ziffer_2}'
    if operation == '+':
        richtige_anwort = str(ziffer_1 + ziffer_2)
    elif operation == '-':
        richtige_anwort = str(ziffer_1 - ziffer_2)
    else:
        richtige_anwort = str(ziffer_1 * ziffer_2)
    return result, richtige_anwort

def brain_calc():
    print("Welcome to the Brain Games!")
    name = string('May I have your name? ')
    print('What is the result of the expression?')
    operations = ['+', '-', '*']
    count = 0
    while count < 3:
        operation = random.choice(operations)
        result, richtige_anwort = log_gen_ziffer(operation)
        print(f'Question: {result}')
        user_anwort = str(input('Your answer: '))
        
        if user_anwort == richtige_anwort:
            print('Correct!')
            count += 1
        else:
            print(f"'{user_anwort}' is wrong answer ;(. Correct answer was '{richtige_anwort}'.\nLet's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')

def main():
    brain_calc()




