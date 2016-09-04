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

    def get_move(self, id_move):
        return self._get_data('move/{}'.format(id_move))