#!/usr/bin/env python


from random import randint


TASK = 'What number is missing in the progression?'


def generate_progression():
    length = randint(5, 10)
    step = randint(2, 20)
    sequence = []
    term = 0
    for i in range(1, length + 1):
        term = term + step
        sequence.append(str(term))
    return sequence


def hide_number(sequence):
    index = randint(0, len(sequence) - 1)
    answer = sequence[index]
    sequence[index] = '..'
    question = ' '.join(sequence)
    return question, answer


def generate_round():
    sequence = generate_progression()
    return hide_number(sequence)
