# pylint: disable=missing-docstring
import random
import string

class Game:

    def __init__(self):
        self.grid = []



    def generate_grid(self):
        for _ in range(0,9):
            self.grid.append(random.choice(string.ascii_uppercase))
        return self.grid

    def is_valid(self, word):
        if word == '' :
            return False

        valid = True
        grille = self.grid.copy()
        for letter in word:
            if letter in grille:
                valid = valid and True
                grille.remove(letter)
            else:
                valid = valid and False
        return valid
