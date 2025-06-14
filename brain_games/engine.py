import prompt

count = 3

def play(game_module):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game_module.beschreibung)

    for i in range(count):
        question, correct_answer = game_module.log_gen_ziffer()

        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"{answer} is wrong answer ;(."
                  f"Correct answer was {correct_answer}"
                  f"\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')