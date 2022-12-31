from lol_python.lol_api_client import LolApiClient
from lol_python.lol_api_version import LolApiVersion


class LoLSummonerClient(LolApiClient):

    def __init__(self, transport):
        super().__init__(transport)
        self.obj_desc = 'Summoner'
        self.v = LolApiVersion.v['summoner']

    def ids(self, summoner_name):
        path = f'/lol/summoner/{self.v}/summoners/by-name/{summoner_name}'
        return self._get(
            path=path, obj_desc=self.obj_desc, route_type='platform')
