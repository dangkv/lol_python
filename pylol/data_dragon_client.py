from pylol.lol_api_client import LolApiClient

class DataDragonClient(LolApiClient):

    def __init__(self, transport):
        super().__init__(transport)
        self.route_type = 'data_dragon'
        self.obj_desc = 'Data Dragon'

        # Asssumption: First element is the latest version
        self.v = self.get_versions()[0]

    def get_versions(self):
        # https://developer.riotgames.com/docs/lol#data-dragon_versions
        path = '/api/versions.json'
        return self._get(path, self.obj_desc, self.route_type)

    def champions(self, version = None):
        v = version if version is not None else self.v
        path = f'/cdn/{v}/data/en_US/champion.json'
        return self._get(path, self.obj_desc, self.route_type)

    def items(self, version = None):
        v = version if version is not None else self.v
        path = f'/cdn/{v}/data/en_US/item.json'
        return self._get(path, self.obj_desc, self.route_type)

    def summoner_spells(self, version = None):
        v = version if version is not None else self.v
        path = f'/cdn/{v}/data/en_US/summoner.json'
        return self._get(path, self.obj_desc, self.route_type)
