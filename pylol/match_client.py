from pylol.lol_api_client import LolApiClient
from pylol.lol_api_version import LolApiVersion


class LoLMatchClient(LolApiClient):

    def __init__(self, transport):
        super().__init__(transport)
        self.obj_desc = 'Match'
        self.v = LolApiVersion.v['match']

    def list(self, puuid, start: int = 0, count: int = 20):
        path = f'/lol/match/{self.v}/matches/by-puuid/{puuid}/' \
               f'ids?start={start}&count={count}'
        return self._get(path=path, obj_desc=self.obj_desc,
                         route_type='region')

    def summary(self, match_id):
        path = f'/lol/match/v5/matches/{match_id}'
        return self._get(path=path, obj_desc=self.obj_desc
                         , route_type='region')

    def timeline(self, match_id):
        path = f'/lol/match/v5/matches/{match_id}/timeline'
        return self._get(path=path, obj_desc=self.obj_desc
                         , route_type='region')
