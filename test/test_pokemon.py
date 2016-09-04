#!/usr/bin/env python
import unittest
from pokelife.pokemon import Pokemon


class TestPokemon(unittest.TestCase):
    def test_pokemon_init(self):
        pokemon = Pokemon(12)
        self.assertEqual(pokemon.name, 'butterfree')
        self.assertEqual(pokemon.speed['base_stat'], 70)
        self.assertCountEqual(pokemon.types, ['flying', 'bug'])