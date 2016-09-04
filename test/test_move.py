#!/usr/bin/env python
import unittest
from pokelife.move import Move


class TestMove(unittest.TestCase):
    def test_move_init(self):
        move = Move(1)
        self.assertEqual(move.name, 'pound')
        self.assertEqual(move.crit_rate, 0)
        self.assertEqual(move.type, 'normal')
        self.assertEqual(move.damage_class, 'physical')
        self.assertEqual(move.ailment, 'none')