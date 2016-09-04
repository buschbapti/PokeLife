#!/usr/bin/env python
from .pokeapi_connect import PokeAPIConnect


class Nature(object):
    def __init__(self, id_nature):
        api = PokeAPIConnect()
        nature_data = api.get_nature(id_nature)
        self.id = nature_data['id']
        self.name = nature_data['name']
        if nature_data['decreased_stat']:
            self.decreased_stat = nature_data['decreased_stat']['name']
        if nature_data['increased_stat']:    
            self.increased_stat = nature_data['increased_stat']['name']

    def __str__(self):
        return self.name