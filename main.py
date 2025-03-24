import signal
import sys
from game.hangman import Hangman
from game.session import GameSession
from game.logger import GameLogger

def signal_handler(sig, frame):
    print("\nExiting game...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


def main():
    words_file = "words.csv"
    hangman = Hangman(words_file)
    logger = GameLogger()
    game_session = GameSession(hangman, logger)
    game_session.start()

if __name__ == "__main__":
    main()





