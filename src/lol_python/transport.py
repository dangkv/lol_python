import requests


class LoLAPITransport:
    def __init__(self, api_key, platform_routing, region_routing):
        self.api_key = api_key
        self.platform_routing = self._get_platform_host(platform_routing)
        self.region_routing = self._get_region_host(region_routing)
        self.data_dragon = self._get_data_dragon_host()

    @staticmethod
    def _get_platform_host(platform_routing):
        hosts = {
            'BR1': 'https://br1.api.riotgames.com',
            'EUN1': 'https://eun1.api.riotgames.com',
            'EUW1': 'https://euw1.api.riotgames.com',
            'JP1': 'https://jp1.api.riotgames.com',
            'KR': 'https://kr.api.riotgames.com',
            'LA1': 'https://la1.api.riotgames.com',
            'LA2': 'https://la2.api.riotgames.com',
            'NA1': 'https://na1.api.riotgames.com',
            'OC1': 'https://oc1.api.riotgames.com',
            'TR1': 'https://tr1.api.riotgames.com',
            'RU': 'https://ru.api.riotgames.com',
        }
        host = hosts.get(platform_routing)

        if host is None:
            raise KeyError(f'{platform_routing} is not a valid Platform '
                           'Routing Value\nFor details visit: '
                           'https://developer.riotgames.com/docs/lol')

        return host

    @staticmethod
    def _get_region_host(region_routing):
        hosts = {
            'AMERICAS': 'https://americas.api.riotgames.com',
            'ASIA': 'https://asia.api.riotgames.com',
            'EUROPE': 'https://europe.api.riotgames.com',
        }
        host = hosts.get(region_routing)

        if host is None:
            raise KeyError(f'{region_routing} is not a valid Region '
                           'Routing Value\nFor details visit: '
                           'https://developer.riotgames.com/docs/lol')

        return host

    @staticmethod
    def _get_data_dragon_host():
        return 'https://ddragon.leagueoflegends.com'

    @staticmethod
    def request(url, method, headers, params=None, body=None):
        request_args = {'method': method, 'url': url, 'headers': headers,
                        'params': params, 'data': body}
        return requests.request(**request_args)

    def _headers_default_receive_json(self):
        return {
            'Origin': 'https://developer.riotgames.com',
            'X-Riot-Token': f'{self.api_key}',
            'Accept': 'application/json'
        }

    def get(self, url, params={}):
        headers = self._headers_default_receive_json()
        return self.request(url, HTTPMethod.GET, headers, params)


class HTTPMethod:
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'
