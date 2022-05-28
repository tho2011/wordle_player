from colorama import Fore, Style


class Wordle:
    def __init__(self, target_word, accepted_words):
        assert target_word in accepted_words
        self.guesses = []
        self.target_word = target_word
        self.accepted_words = accepted_words

    def show(self):
        for word in self.guesses:
            print(word)
        print()

    def add_guess(self, guess):
        counts = {}
        colors = [Fore.WHITE] * 5

        target_rem = []
        guess_rem = []

        for i, ch in enumerate(guess):
            if ch == self.target_word[i]:
                colors[i] = Fore.GREEN
            else:
                target_rem.append(self.target_word[i])
                guess_rem.append((ch, i))

        for s in guess_rem:
            if s[0] in target_rem:
                colors[s[1]] = Fore.YELLOW
                target_rem.remove(s[0])

        self.guesses.append(
            f"{colors[0]}{guess[0]}{colors[1]}{guess[1]}{colors[2]}{guess[2]}{colors[3]}{guess[3]}{colors[4]}{guess[4]}{Style.RESET_ALL}"
        )

    def play(self):
        while True:
            self.show()
            guess = input(f"Input guess {len(self.guesses) + 1}: ")
            print()
            while (guess not in self.accepted_words) or (guess in self.guesses):
                print("Invalid guess.")
                guess = input(f"Input guess {len(self.guesses) + 1}: ")
                print()

            self.add_guess(guess)

            if guess == self.target_word:
                try_num = len(self.guesses)
                if try_num == 1:
                    print(f"Guessed in 1 try")
                else:
                    print(f"Guessed in {try_num} tries")
                print()
                break

            if len(self.guesses) == 6:
                break

        self.show()
        print("Game Over")


def main():
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
