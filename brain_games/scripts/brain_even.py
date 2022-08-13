#!/usr/bin/env python


from brain_games.logic.even import is_even
from brain_games.logic.even import question
from brain_games.logic.even import even_odd
from brain_games.logic.greet import welcome


def main():
    name = welcome()
    even_odd(name)


if __name__ == '__main__':
    main()
