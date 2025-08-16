import random
from math import gcd
from brain_games.games.calc import der_anfang, das_ende

beschreibung = 'Find the greatest common divisor of given numbers.'

def log_gen_ziffer():
    a = random.randrange(der_anfang, das_ende) #NOSONAR
    b = random.randrange(der_anfang, das_ende) #NOSONAR
    question = f'{a} {b}'
    correct_answer = gcd(a, b)
    return question, str(correct_answer)
