#!/usr/bin/env python
from .pokeapi_connect import PokeAPIConnect
from .move import Move
from .nature import Nature
from .const import *
from numpy.random import randint


class Pokemon(object):
    def __init__(self, id_pokemon):
        api = PokeAPIConnect()
        # connect to pokeapi to get infos such as name and base states
        pokemon_data = api.get_pokemon(id_pokemon)
        self.id = pokemon_data['id']
        self.name = pokemon_data['name']
        # set default base_stat
        for s in pokemon_data['stats']:
            setattr(self, s['stat']['name'], {'base_stat':s['base_stat'], 'effort':s['effort']})
        # set possible abilities
        self.available_abilities = [a['ability']['name'] for a in pokemon_data['abilities']]
        self.available_moves = [m['move']['name'] for m in pokemon_data['moves']]
        self.types = [t['type']['name'] for t in pokemon_data['types']]
        # set empty values for nature, moves and abilities 
        self.nature = Nature(randint(MAX_NATURE))
        self.ability = self.available_abilities[randint(len(self.available_abilities))]
        self.moves = [self.available_moves[i] for i in randint(len(self.available_moves), size=4)]

    @property
    def ability(self):
        return self.__ability
    
    @ability.setter
    def ability(self, ability):
        assert ability in self.available_abilities, "%r is not in the list of available abilities" % ability
        self.__ability = ability

    def set_ability_by_index(self, index):
        assert type(index) is int, "Choosen index is not an integer: %r" % index
        assert index >= 0 and index <= len(self.available_abilities), "Incorrect index, outside of the list size: %r" % index
        self.__ability = self.available_abilities[index]

    @property
    def nature(self):
        return self.__nature
    
    @nature.setter
    def nature(self, id_nature):
        self.__nature = Nature(id_nature)

    @property
    def moves(self):
        return self.__moves

    @moves.setter
    def moves(self, moves):
        assert len(moves) == 4, "The list of moves should contain four elements"
        move_pool = []
        for m in moves:
            move = Move(m)
            assert move.name in self.available_moves, "%r is not in the list of available moves" % move
            move_pool.append(move)
        self.__moves = move_pool

    def set_move_at_index(self, move_number, id_move):
        assert move_number <= 0 or move_number > 4, "The choosen move index should be between 0 and 3"
        # set the list of four active moves
        move = Move(id_move)
        assert move.name in self.available_moves, "%r is not in the list of available moves" % move
        self.__moves[move_number] = move

    def __str__(self):
        attrs = {key:value for key, value in self.__dict__.items() if not key.startswith('__') and not callable(key)}
        return '\n'.join("%s: %s" % item for item in attrs.items())