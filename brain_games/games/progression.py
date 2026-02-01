from random import randint

description = 'What number is missing in the progression?'
START = 1
STOP = 50
STEP_START = 3
STEP_STOP = 10
PROGRESSION_LENGTH_START = 5
PROGRESSION_LENGTH_STOP = 10


def log_gen_ziffer():

    progression = []
    number = randint(START, STOP)  # NOSONAR
    step = randint(STEP_START, STEP_STOP)  # NOSONAR
    length = randint(PROGRESSION_LENGTH_START, PROGRESSION_LENGTH_STOP)  # NOSONAR
    for _ in range(length):
        progression.append(number)
        number = number + step
    correct_answer = progression[randint(0, len(progression) - 1)]  # NOSONAR
    correct_answer_index = progression.index(correct_answer)
    progression[correct_answer_index] = '..'
    progression = ' '.join(map(str, progression))
    question = f'{progression}'
    return question, str(correct_answer)
