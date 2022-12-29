#!/usr/bin/env python

from random import randint
from math import sqrt
from brain_games.cli import generate_answer


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUM = 2
MAX_NUM = 100


def is_prime(number):
    '''Checks if a number is prime'''
    sqrt_number = int(sqrt(number))
    for num in range(2, sqrt_number + 1):
        if number % num == 0:
            return False
    return True


def generate_round(number=None):
    '''Generates a question from passed arguments or randomly chooses them'''
    if number is None:
        number = randint(MIN_NUM, MAX_NUM)
    question = str(number)
    right_answer = generate_answer(is_prime(number))
    return question, right_answer
