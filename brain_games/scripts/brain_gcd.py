#!/usr/bin/env python


from brain_games.engine import start_game
from brain_games.logic import gcd


def main():
    start_game(gcd)


if __name__ == '__main__':
    main()