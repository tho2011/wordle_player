from colorama import Fore, Style
from wordle import Wordle
import random

def main():
    # valid_words = "us_list.txt"
    valid_words = "valid_wordle_words.txt"
    targets = "us_solutions.txt"

    with open(valid_words, "r") as file:
         us_list = [word.strip().replace('"','') for word in file.read().split(',')]

    with open(targets, "r") as file:
         us_soln = [word.strip().replace('"','') for word in file.read().split(',')]

    us_soln.sort()

    game = Wordle(random.choice(us_soln), us_list+us_soln)
    game.play()




if __name__ == "__main__":
    main()
