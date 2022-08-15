#!/usr/bin/env python


import prompt


ROUNDS = 3


def start_game(game):
    """The main engine of the game"""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.TASK)
    
    for round in range(ROUNDS):
        question, right_answer = game.generate_round()
        print(f'Question: {question}')
        player_answer = prompt.string('Your answer: ')
        
        if player_answer == right_answer:
            print('Correct!')
        else:
            message = "'{}' is wrong answer ;(. Correct answer was '{}'"
            print(message.format(player_answer, right_answer))
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
    return
