#!/usr/bin/env python


from random import randint, choice


TASK = 'What is the result of the expression?'


def calculate(num1, num2, oper):
    if oper == '+':
        return str(num1 + num2)
    if oper == '-':
        return str(num1 - num2)
    if oper == '*':
        return str(num1 * num2)


def generate_round():
    number1 = randint(1, 25)
    number2 = randint(1, 25)
    operations = ['+', '-', '*']
    operator = choice(operations)
    question = f'{number1} {operator} {number2}'
    right_answer = calculate(number1, number2, operator)
    return question, right_answer
