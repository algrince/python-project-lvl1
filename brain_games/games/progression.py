#!/usr/bin/env python


from random import randint


TASK = 'What number is missing in the progression?'
MIN_LEN = 5
MAX_LEN = 10
MIN_STEP = 2
MAX_STEP = 20


def generate_progression(length, step):
    '''Generates progression of stated size'''
    sequence = []
    term = 0
    for i in range(1, length + 1):
        term = term + step
        sequence.append(term)
    return sequence


def generate_question(sequence, index):
    '''Hides chosen element of sequence and returns sequence as string'''
    sequence[index] = '..'
    question = ' '.join([str(num) for num in sequence])
    return question


def generate_round(
    length=None,
    step=None,
    index=None,
):
    '''Generates a question from passed arguments or randomly chooses them'''
    if length is None:
        length = randint(MIN_LEN, MAX_LEN)
    if step is None:
        step = randint(MIN_STEP, MAX_STEP)
    if index is None:
        index = randint(0, length - 1)
    sequence = generate_progression(length, step)
    right_answer = str(sequence[index])
    question = generate_question(sequence, index)
    return question, right_answer
