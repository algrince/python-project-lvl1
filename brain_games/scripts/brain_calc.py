#!/usr/bin/env python


from brain_games.engine import play_game
from brain_games.games import calc


def main():
    play_game(calc)


if __name__ == '__main__':
    main()
