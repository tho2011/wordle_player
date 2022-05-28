from colorama import Fore, Style
from string import ascii_lowercase
import random

def is_fixed_at(word, fixed):
    return True if not fixed else all(word[key] == fixed[key] for key in fixed.keys())

def not_contains(word,exclude):
    return True if not exclude else all(ch not in word for ch in exclude)

def not_in_pos(word, anti_position):
    if not anti_position:
        return True

    pos_checks = []
    char_includes = []

    for key in anti_position.keys():
        pos_checks.append(word[key] != anti_position[key])

    for value in set(anti_position.values()):
        char_includes.append(value in word)

    return all(pos_checks) and all(char_includes)

class Wordle:

    def __init__(self, target_word, accepted_words, initial_guess="crane", display_keyboard=True, is_notebook=False):

        self.c_map = {0:Fore.BLACK , 1:Fore.WHITE, 2:Fore.YELLOW, 3:Fore.GREEN}
        if is_notebook:
            self.c_map[0] = Fore.WHITE
            self.c_map[1] = Fore.BLACK

        self.keyboard_colors = {}
        for ch in ascii_lowercase:
            self.keyboard_colors[ch] = 1

        self.guesses = []
        self.target_word = target_word
        self.accepted_words = accepted_words
        self.initial_guess = initial_guess
        self.candidates = accepted_words.copy()
        self.display_keyboard = display_keyboard

    def show(self):
        for word in self.guesses:
            print(word)
        print()
        if self.display_keyboard:
            my_str = "".join(f"""{self.c_map[self.keyboard_colors[ch]]}{ch}""" for ch in ascii_lowercase)
            print(my_str+Style.RESET_ALL+"\n")

    def add_guess(self, guess):
        counts = {}
        colors = [Fore.WHITE] * 5

        target_rem = []
        guess_rem = []

        fixed = {}
        exclude = set()
        anti_position = {}

        for i, ch in enumerate(guess):
            if ch == self.target_word[i]:
                colors[i] = Fore.GREEN
                self.keyboard_colors[ch] = 3
                fixed[i] = ch
            else:
                target_rem.append(self.target_word[i])
                guess_rem.append((ch, i))

        for s in guess_rem:
            if s[0] in target_rem:
                colors[s[1]] = Fore.YELLOW
                anti_position[s[1]] = s[0]
                target_rem.remove(s[0])
                if self.keyboard_colors[s[0]] == 1:
                    self.keyboard_colors[s[0]] = 2
            else:
                if (s[0] not in fixed.values()) and (s[0] not in anti_position.values()):
                    self.keyboard_colors[s[0]] = 0
                    exclude.add(s[0])

        self.guesses.append("".join(f"""{col}{ch}""" for col,ch in zip(colors,guess)))

        return fixed, exclude, anti_position




    def __apply_filter(self,fixed,exclude,anti_position):
        result = []
        for word in self.candidates:
            if is_fixed_at(word,fixed) and not_contains(word, exclude) and not_in_pos(word,anti_position):
                result.append(word)
    # return result
        self.candidates = result


    def play(self):

        fixed, exclude, anti_position = self.add_guess(self.initial_guess)
        self.show()
        if self.initial_guess == self.target_word:
            print(f"Guessed in 1 try")
        else:
            while True:
                self.__apply_filter(fixed, exclude, anti_position)
                guess = random.choice(self.candidates)
                fixed, exclude, anti_position = self.add_guess(guess)
                self.show()

                if guess == self.target_word:
                    try_num = len(self.guesses)
                    print(f"Guessed in {try_num} tries")
                    print()
                    break

                if len(self.guesses) == 6:
                    print(self.target_word)
                    break

        # self.show()
        # print(self.target_word)
        print("Game Over\n")


def main():
    # rooto is not a real word but we used it to test
    # the logic for yellow coloring
    valid_list = [
        "acids",
        "belts",
        "adieu",
        "adore",
        "nests",
        "fresh",
        "pizza",
        "robot",
        "rooto",
    ]
    game = Wordle("robot", valid_list)
    game.play()


if __name__ == "__main__":
    main()
