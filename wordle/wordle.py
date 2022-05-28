from colorama import Fore, Style
from string import ascii_lowercase

c_map = {1:Fore.BLACK , 0:Fore.WHITE, 2:Fore.YELLOW, 3:Fore.GREEN}

class Wordle:

    def __init__(self, target_word, accepted_words):
        # assert target_word in accepted_words

        self.keyboard_colors = {}
        for ch in ascii_lowercase:
            self.keyboard_colors[ch] = 1

        self.guesses = []
        self.target_word = target_word
        self.accepted_words = accepted_words

    def show(self):
        for word in self.guesses:
            print(word)
        print()
        my_str = "".join(f"""{c_map[self.keyboard_colors[ch]]}{ch}""" for ch in ascii_lowercase)
        print(my_str+Style.RESET_ALL+"\n")

    def add_guess(self, guess):
        counts = {}
        colors = [Fore.WHITE] * 5

        target_rem = []
        guess_rem = []

        for i, ch in enumerate(guess):
            if ch == self.target_word[i]:
                colors[i] = Fore.GREEN
                self.keyboard_colors[ch] = 3
            else:
                target_rem.append(self.target_word[i])
                guess_rem.append((ch, i))

        for s in guess_rem:
            if s[0] in target_rem:
                colors[s[1]] = Fore.YELLOW
                target_rem.remove(s[0])
                if self.keyboard_colors[s[0]] == 1:
                    self.keyboard_colors[s[0]] = 2
            else:
                self.keyboard_colors[s[0]] = 0

        self.guesses.append("".join(f"""{col}{ch}""" for col,ch in zip(colors,guess)))

    def play(self):
        while True:
            guess = input(f"Input guess {len(self.guesses) + 1}: ")
            print()
            while (guess not in self.accepted_words):
                print("Invalid guess.")
                guess = input(f"Input guess {len(self.guesses) + 1}: ")
                print()

            self.add_guess(guess)

            self.show()

            if guess == self.target_word:
                try_num = len(self.guesses)
                if try_num == 1:
                    print(f"Guessed in 1 try")
                else:
                    print(f"Guessed in {try_num} tries")
                print()
                break

            if len(self.guesses) == 6:
                print(self.target_word)
                break

        # self.show()
        # print(self.target_word)
        print("Game Over")


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
