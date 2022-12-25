#!/usr/bin/env python


from random import randint, choice


TASK = 'What is the result of the expression?'
OPERATIONS = ['+', '-', '*']


def generate_vars(min_num, max_num):
    '''Generates two numbers in passed interval and an operator'''
    number1 = randint(min_num, max_num)
    number2 = randint(min_num, max_num)
    operator = choice(OPERATIONS)
    return number1, number2, operator


def calculate(num1, num2, oper):
    '''Calculates the right answer to the expression'''
    if oper == '+':
        return num1 + num2
    if oper == '-':
        return num1 - num2
    if oper == '*':
        return num1 * num2


def generate_round(**kwargs):
    '''Generates a question from passed arguments or randomly chooses them'''
    if kwargs:
        number1 = kwargs['number1']
        number2 = kwargs['number2']
        operator = kwargs['operator']
    else:
        number1, number2, operator = generate_vars(1, 25)
    question = f'{number1} {operator} {number2}'
    right_answer = str(calculate(number1, number2, operator))
    return question, right_answer
