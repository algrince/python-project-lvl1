#!/usr/bin/env python


from random import randint, choice


TASK = 'What is the result of the expression?'
OPERATIONS = ['+', '-', '*']
MIN_NUM1 = 1
MAX_NUM1 = 25
MIN_NUM2 = 1
MAX_NUM2 = 25


def calculate(num1, num2, oper):
    '''Calculates the right answer to the expression'''
    if oper == '+':
        return num1 + num2
    if oper == '-':
        return num1 - num2
    if oper == '*':
        return num1 * num2


def generate_round(
    number1=None,
    number2=None,
    operator=None,
):
    '''Generates a question from passed arguments or randomly chooses them'''
    if number1 is None:
        number1 = randint(MIN_NUM1, MAX_NUM1)
    if number2 is None:
        number2 = randint(MIN_NUM2, MAX_NUM2)
    if operator is None:
        operator = choice(OPERATIONS)
    question = f'{number1} {operator} {number2}'
    right_answer = str(calculate(number1, number2, operator))
    return question, right_answer
