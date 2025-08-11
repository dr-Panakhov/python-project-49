import random

beschreibung = 'Answer "yes" if the number is even, otherwise answer "no".'


# Логика задачи
def log_gen_ziffer():
    def is_even(number):
        if number % 2 == 0:
            return True
        else:
            return False
    number = random.randrange(1, 100)
    frage = f'{number}'
    if is_even(number):
        correct_anwort = 'yes'
    else:
        correct_anwort = 'no'
    return frage, correct_anwort


