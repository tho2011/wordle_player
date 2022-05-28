from colorama import Fore, Style
import wordle_random
import random

def main():
    # valid_words = "us_list.txt"
    valid_words = "../wordle/valid_wordle_words.txt"
    targets = "../wordle/us_solutions.txt"

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
    game = wordle_random.Wordle(random.choice(us_soln), us_list+us_soln, display_keyboard=True)
    game.play()




if __name__ == "__main__":
    main()
