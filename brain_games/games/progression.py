#!/usr/bin/env python


from random import randint


TASK = 'What number is missing in the progression?'


def generate_vars(length_size, step_size):
    '''Generates length and step of progression
        with an index of the number to hide'''
    min_len, max_len = length_size
    min_step, max_step = step_size
    length = randint(min_len, max_len)
    step = randint(min_step, max_step)
    index = randint(0, length - 1)
    return length, step, index


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


def generate_round(**kwargs):
    '''Generates a question from passed arguments or randomly chooses them'''
    if kwargs:
        length = kwargs['length']
        step = kwargs['step']
        index = kwargs['index']
    else:
        length, step, index = generate_vars((5, 10), (2, 20))
    sequence = generate_progression(length, step)
    right_answer = str(sequence[index])
    question = generate_question(sequence, index)
    return question, right_answer
