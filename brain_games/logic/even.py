#!/usr/bin/env python


import prompt
from random import randint


def is_even(num):
    """Returns 'yes' if the given number is even and 'no' if it is not"""
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def question(right_count, name):
    """Generates a random number and asks the player to say if it is even or not;
    rensponds to player if thier answer is correct and returns a renewed count of
    right answers"""
    number = randint(1, 100)
    print('Question: ' + str(number))
    answer = prompt.string('Your answer: ')
    if answer == is_even(number):
        print('Correct!')
        right_count = right_count + 1
    else:
        print("'" + answer + "'" + ' is wrong answer ;(. Correct answer was ' + 
                "'" + is_even(number) + '"')
        print("Let's try again, " + name)
        right_count = 0
    return right_count


def even_odd(name):
    """Starts and finishes even or odd game"""
    print('Answer "yes" if the number is even, otherwise answer "no".') 
    right_count = 0
    while right_count < 3:
        right_count = question(right_count, name)
    print('Congratulations, ' + name + '!')
