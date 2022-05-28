from colorama import Fore, Style
from wordle import Wordle
import random

def main():
    # valid_words = "us_list.txt"
    valid_words = "valid_wordle_words.txt"
    targets = "us_solutions.txt"

    us_list = []
    us_soln = []


    with open(valid_words, "r") as file:
        for line in file:
            for word in line.split(','):
                us_list.append(word.replace('"','').strip())

    with open(targets, "r") as file:
        for line in file:
            for word in line.split(','):
                us_soln.append(word.replace('"','').strip())

    # print(len(us_list))
    # print(len(us_soln))

    us_soln.sort()
    #
    game = Wordle(random.choice(us_soln), us_list+us_soln)
    game.play()




if __name__ == "__main__":
    main()
