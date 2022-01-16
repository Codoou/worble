import random
import string

class WorbleGame:
    ROUNDS = 5
    KEYS = ['first', 'second', 'third', 'fourth', 'fifth']
    
    def __init__(self):

        self._word_dict, self._word_list = self._build_words()
        self._word = random.choice(self._word_list)
        self._split_word = self._word_dict[self._word]
        self.available_letters = list(string.ascii_lowercase)
        self.used_misplaced_letters = []


    def play_round(self, round_number=1):
        if round_number > self.ROUNDS:
            self.loser()

        print("============================================")
        print("Round Number: ", str(round_number))
        print("Available Letters: ", self.available_letters)

        
        word = self.input_word()
        if self.validate_word(word):
            self.winner()

        round_number += 1
        self.play_round(round_number)

    def validate_word(self, word):
        """"""
        validated = False

        if word == self._word:
            validated = True
            return validated

        word_dict = self._dict_conversion(word)
        # print(word_dict)

        for placement in self.KEYS:
            if self._dict_compare(word_dict, self._split_word, placement):
                """"""
                print(f"Letter '{word_dict[placement]}' at {placement} is correct.")
                self.black_list_letter(word_dict[placement])

            elif self._list_compare(word_dict[placement]):
                """"""
                print(f"Letter '{word_dict[placement]}' is a correct letter, but not in the correct space.")
            else:
                self.black_list_letter(word_dict[placement])

        return validated

    def black_list_letter(self, letter):
        """"""
        self.available_letters.remove(letter)

    def _list_compare(self, letter):
        """"""
        if letter in self._word:
            return True
        return False


    def _dict_compare(self, first, second, key):
        if first[key] == second[key]:
            return True

        return False

    def input_word(self, word=''):
        if len(word) > 0:
            return word

        word = input("Enter 5 letter word: ")
        print(word)

        if word not in self._word_list:
            print(f"'{word}' is not a valid word. Please try again.")
            word = self.input_word(word)
            return word

        return word


    def winner(self):
        print("You won, the correct word was: ", self.reveal())
        raise

    def loser(self):
        print("You lost, the correct answer was: ", self.reveal())
        raise

    def reveal(self):
        return self._word

    def _build_words(self):
        word_dict  = {}
        word_list = []

        with open("words.txt") as f:
            words = f.readlines()
            for word in str(words).split(" "):
                word = word.replace("'","").replace("]","").replace("[","").strip()
                if len(set(word)) == len(word):
                    word_list.append(word)
                    word_dict[word] = self._dict_conversion(word)

        return word_dict, word_list

    def _dict_conversion(self, word):
        return {
            "first": word[0],
            "second": word[1],
            "third": word[2],
            "fourth": word[3],
            "fifth": word[4]
        }



worble = WorbleGame()
worble.play_round()