#!/usr/bin/env python


from random import randint

TASK = "Find the greatest common divisor of given numbers."


def find_gcd(num1, num2):
    gcd = 1
    for number in range(1, min(num1, num2)):
        if num1 % number == 0 and num2 % number == 0:
            gcd = number
    return str(gcd)


def generate_round():
    number1 = randint(2, 100)
    number2 = randint(2, 100)
    question = f'{number1} {number2}'
    return question, find_gcd(number1, number2)
