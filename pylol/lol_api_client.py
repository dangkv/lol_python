import requests


class LolApiClient:

    def __init__(self, transport):
        self.transport = transport

    def _get(self, path, obj_desc, route_type, **kwargs):
        if route_type == 'platform':
            host = self.transport.platform_routing
        elif route_type == 'region':
            host = self.transport.region_routing
        elif route_type == 'data_dragon':
            host = self.transport.data_dragon
        else:
            raise ValueError(
                f'Error retrieving {obj_desc}: Invalid Route Type {route_type}')

        uri = host + path
        response = self.transport.get(url=uri, params=kwargs)

        if response.status_code == requests.codes.OK:
            return response.json()
        else:
            raise Exception(f'Error retrieving {obj_desc}: {response.text}')
