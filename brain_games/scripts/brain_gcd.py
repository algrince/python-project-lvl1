#!/usr/bin/env python


from brain_games.engine import play_game
from brain_games.games import gcd


def main():
    play_game(gcd)


if __name__ == '__main__':
    main()
