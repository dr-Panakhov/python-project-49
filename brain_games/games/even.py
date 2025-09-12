import random

from brain_games.games.calc import start_n, stop_n

description = 'Answer "yes" if the number is even, otherwise answer "no".'


# Логика задачи
def log_gen_ziffer():
    def is_even(number):
        if number % 2 == 0:
            return True
        else:
            return False
    number = random.randrange(start_n, stop_n) #NOSONAR
    question = f'{number}'
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


