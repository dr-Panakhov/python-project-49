import random
import prompt
# Приветствие
print("Welcome to the Brain Games!")
name = prompt.string('May I have your name? ')
print(f'Hello, {name}!\nAnswer "yes" if the number is even, otherwise answer "no"')
# Логика задачи
def is_even():
    richtige_anwort = 0
    while richtige_anwort < 3:
        ziffer = random.randrange(0,100)
        print(f"Question: {ziffer}")
        user_antwort = input("Your answer: ").lower()
        if (ziffer % 2 == 0 and user_antwort == 'yes') or (ziffer % 2 != 0 and user_antwort == 'no'):
            print('Correct!')
            richtige_anwort = richtige_anwort +1
        else:
            print(f"'{user_antwort}' is wrong answer ;(. Correct answer was {"'yes'" if ziffer % 2 == 0 else "'no'"}.\nLet's try again, {name}!")
            break
    if richtige_anwort == 3:
        print(f"Congratulations, {name}!")
is_even()