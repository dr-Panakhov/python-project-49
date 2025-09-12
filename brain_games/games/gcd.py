import random
from math import gcd
from brain_games.games.calc import start_n, stop_n

description = 'Find the greatest common divisor of given numbers.'

def log_gen_ziffer():
    a = random.randrange(start_n, stop_n) #NOSONAR
    b = random.randrange(start_n, stop_n) #NOSONAR
    question = f'{a} {b}'
    correct_answer = gcd(a, b)
    return question, str(correct_answer)
