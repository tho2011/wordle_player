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
        self.guesses.append(guess)




    def play(self):
        while(True):
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
    valid_list = ['acids','belts','adieu','adore','nests','fresh','pizza']
    game = Wordle('belts',valid_list)

    game.play()


if __name__ == '__main__':
    main()
