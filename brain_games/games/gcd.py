import random
from math import gcd

beschreibung = 'Find the greatest common divisor of given numbers.'
def log_gen_ziffer():
    a = random.randrange(1, 100)
    b = random.randrange(1, 100)
    question = f'{a} {b}'
    correct_answer = gcd(a, b)
    return question, str(correct_answer)
