import json
import requests


class LoLAPIClient:

    def __init__(self, transport):
        self.transport = transport
        self.url = self.transport.routing

    def _get(self, path, obj_desc):
        uri = self.url + path
        response = self.transport.get(url=uri, params={})
        if response.status_code == requests.codes.OK:
            return response.json()
        else:
            raise Exception(f'Error retrieving {obj_desc}: {response.text}')
