#!/usr/bin/env python
import unittest
from pokelife.pokeapi_connect import PokeAPIConnect


class TestPokeAPIConnect(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api = PokeAPIConnect()

    def test_get_pokemon(self):
        self.assertEqual(self.api.get_pokemon(12)['name'], 'butterfree')

    def test_get_move(self):
        self.assertEqual(self.api.get_move(42)['name'], 'pin-missile')

if __name__ == '__main__':
    unittest.main()