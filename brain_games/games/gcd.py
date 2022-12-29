#!/usr/bin/env python


from random import randint

TASK = "Find the greatest common divisor of given numbers."
MIN_NUM1 = 2
MAX_NUM1 = 100
MIN_NUM2 = 2
MAX_NUM2 = 100


def find_gcd(num1, num2):
    '''Finds the greater common divisor of two passed numbers'''
    if num1 >= num2:
        num1 = num1 % num2
    elif num2 > num1:
        num2 = num2 % num1
    return find_gcd(num1, num2)


def generate_round(
    number1=None,
    number2=None,
):
    '''Generates a question from passed arguments or randomly chooses them'''
    if number1 is None:
        number1 = randint(MIN_NUM1, MAX_NUM1)
    if number2 is None:
        number2 = randint(MIN_NUM2, MAX_NUM2)
    question = f'{number1} {number2}'
    right_answer = str(find_gcd(number1, number2))
    return question, right_answer
