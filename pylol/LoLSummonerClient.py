from pylol.LoLAPIClient import LoLAPIClient


class LoLSummonerClient(LoLAPIClient):

    def __init__(self, transport):
        super().__init__(transport)
        self.obj_desc = 'Summoner'

    def get_details(self, summoner_name):
        path = f'/lol/summoner/v4/summoners/by-name/{summoner_name}'
        return self._get(path=path, obj_desc=self.obj_desc)
