#!/usr/bin/env python

from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise anser "no".'


def is_prime(number):
    for num in range(2, number):
        if number % num == 0:
            return 'no'
    return 'yes'


def generate_round():
    question = randint(2, 100)
    return str(question), is_prime(question)
