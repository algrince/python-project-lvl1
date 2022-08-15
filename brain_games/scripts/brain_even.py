#!/usr/bin/env python


from brain_games.engine import start_game
from brain_games.logic import even


def main():
    start_game(even)


if __name__ == '__main__':
    main()
