#!/usr/bin/env python


from brain_games.engine import start_game
from brain_games.logic import calc


def main():
    start_game(calc)


if __name__ == '__main__':
    main()
