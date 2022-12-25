#!/usr/bin/env python

from random import randint
from math import sqrt
from brain_games.cli import generate_answer


TASK = 'Answer "yes" if given number is prime. Otherwise anser "no".'


def generate_vars(min_num, max_num):
    '''Generates a number in passed interval'''
    return randint(min_num, max_num)


def is_prime(number):
    '''Checks if a number is prime'''
    sqrt_number = int(sqrt(number))
    for num in range(2, sqrt_number + 1):
        if num % sqrt_number == 0:
            return False
    return True


def generate_round(**kwargs):
    '''Generates a question from passed arguments or randomly chooses them'''
    if kwargs:
        number = kwargs['number']
    else:
        number = generate_vars(2, 100)
    question = str(number)
    right_answer = generate_answer(is_prime(number))
    return question, right_answer
