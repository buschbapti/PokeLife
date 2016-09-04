#!/usr/bin/env python
from .pokeapi_connect import PokeAPIConnect


class Move(object):
    """docstring for Move"""
    def __init__(self, id_move):
        api = PokeAPIConnect()
        # connect to pokeapi to get infos such as name and effect
        move_data = api.get_move(id_move)
        data_keys = ['id', 'name', 'accuracy', 'pp', 'priority', 'effect_chance',
                     'type', 'power', 'damage_class', 'stat_changes']
        meta_data_keys = ['min_hits', 'max_hits', 'min_turns', 'max_turns', 'drain',
                          'healing', 'crit_rate', 'ailment_chance', 'flinch_chance',
                          'stat_chance']
        # set class attributes
        for key, value in move_data.items():
            if key in data_keys:
                setattr(self, key, value)
        for key, value in move_data['meta'].items():
            if key in meta_data_keys:
                setattr(self, key, value)
        self.ailment = move_data['meta']['ailment']['name']