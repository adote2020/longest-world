# pylint: disable=missing-docstring
import random
import string
import requests

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

        if valid is True:
            return self.__check_dictionary(word)

        return valid

    @staticmethod
    def __check_dictionary(word):
        response = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        json_response = response.json()
        return json_response['found']
