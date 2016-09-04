#!/usr/bin/env python
import json
import requests


class PokeAPIConnect(object):
    def __init__(self):
        self.base_url = 'http://pokeapi.co/api/v2/'

    def _get_data(self, str_req):
        resp = requests.get(self.base_url + str_req)
        if resp.status_code != 200:
            # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))
        return resp.json()

    def get_pokemon(self, id_pokemon):
        return self._get_data('pokemon/{}'.format(id_pokemon))

    def get_number_of_pokemons(self):
        return self._get_data('pokemon')['count']

    def get_move(self, id_move):
        return self._get_data('move/{}'.format(id_move))

    def get_number_of_moves(self):
        return self._get_data('move')['count']

    def get_nature(self, id_nature):
        return self._get_data('nature/{}'.format(id_nature))

    def get_number_of_natures(self):
        return self._get_data('nature')['count']