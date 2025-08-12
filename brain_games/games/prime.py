from random import randint

beschreibung = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def log_gen_ziffer():
    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, (int(n**0.5) + 1)):
            if n % i == 0:
                return False
        return True

    number = randint(2, 100)
    question = f'{number}'
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer