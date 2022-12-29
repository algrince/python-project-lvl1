#!/usr/bin/env python


from random import randint
from brain_games.cli import generate_answer

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUM = 1
MAX_NUM = 100


def is_even(num):
    '''Checks if number is even or not'''
    return num % 2 == 0


def generate_round(number=None):
    '''Generates a question from passed arguments or randomly chooses them'''
    if number is None:
        number = randint(MIN_NUM, MAX_NUM)
    question = str(number)
    right_answer = generate_answer(is_even(number))
    return question, right_answer
