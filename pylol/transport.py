import requests


class LoLAPITransport:
    def __init__(self, api_key, region):
        self.api_key = api_key
        self.routing = self._get_routing(region)

    @staticmethod
    def _get_routing(region):
        host = {
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
        region_host = host.get(region)

        if region_host is None:
            raise KeyError(f'{region} is not a valid region')

        return region_host

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

    def get(self, url, params):
        headers = self._headers_default_receive_json()
        return self.request(url, HTTPMethod.GET, headers, params)


class HTTPMethod:
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'
