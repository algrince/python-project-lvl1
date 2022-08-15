#!/usr/bin/env python


from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    """Returns 'yes' if the given number is even and 'no' if it is not"""
    return 'yes' if num % 2 == 0 else 'no'


def generate_round():
    """Generates a random number and returns it with info is it's even"""
    number = randint(1, 100)
    return str(number), is_even(number)
