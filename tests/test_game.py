import unittest
import string
from game import Game

class Testgame(unittest.TestCase):
    def test_game_iniyilization(self):
        new_game = Game()
        grid = new_game.generate_grid()
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def test_empty_word_is_invalid(self):
        new_game = Game()
        self.assertIs(new_game.is_valid(''), False)

    def test_is_valid(self):
        new_game = Game()
        new_game.grid = list('KWEUEAKRZ')
        self.assertIs(new_game.is_valid('EUREKA'), True)
        self.assertEqual(new_game.grid, list('KWEUEAKRZ'))

    def test_is_invalid(self):
        new_game = Game()
        new_game.grid = list('KWEUEAKRZ')
        self.assertIs(new_game.is_valid('EUREKAA'), False)
        self.assertEqual(new_game.grid, list('KWEUEAKRZ'))

    def test_unknown_word_is_invalid(self):
        new_game = Game()
        new_game.grid = list('KWIENFUQW')
        self.assertIs(new_game.is_valid('FEUN'), False)
