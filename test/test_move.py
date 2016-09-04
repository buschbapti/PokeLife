#!/usr/bin/env python
import unittest
from pokelife.move import Move


class TestPokeAPIConnect(unittest.TestCase):
    def test_move_init(self):
        move = Move(1)
        self.assertEqual(move.name, 'pound')
        self.assertEqual(move.crit_rate, 0)
        self.assertEqual(move.ailment, 'none')