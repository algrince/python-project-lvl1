#!/usr/bin/env python


from random import randint
from brain_games.cli import generate_answer

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_vars(min_num, max_num):
    '''Generates a number in passed interval'''
    return randint(min_num, max_num)


def is_even(num):
    '''Checks if number is even or not'''
    return num % 2 == 0


def generate_round(**kwargs):
    '''Generates a question from passed arguments or randomly chooses them'''
    if kwargs:
        number = kwargs['number']
    else:
        number = generate_vars(1, 100)
    question = str(number)
    right_answer = generate_answer(is_even(number))
    return question, right_answer
