#!/usr/bin/env python


from random import randint

TASK = "Find the greatest common divisor of given numbers."


def generate_vars(min_num, max_num):
    '''Generates two numbers in passed interval'''
    number1 = randint(min_num, max_num)
    number2 = randint(min_num, max_num)
    return number1, number2


def find_gcd(num1, num2):
    '''Finds the greater common divisor of two passed numbers'''
    if num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 = num1 % num2
        elif num2 > num1:
            num2 = num2 % num1
        return find_gcd(num1, num2)
    else:
        return num1 + num2


def generate_round(**kwargs):
    '''Generates a question from passed arguments or randomly chooses them'''
    if kwargs:
        number1 = kwargs['number1']
        number2 = kwargs['number2']
    else:
        number1, number2 = generate_vars(2, 100)
    question = f'{number1} {number2}'
    right_answer = str(find_gcd(number1, number2))
    return question, right_answer
