from lol_python.data_dragon_client import DataDragonClient
from lol_python.match_client import LoLMatchClient
from lol_python.summoner_client import LoLSummonerClient
from lol_python.transport import LoLAPITransport


class lol_python:
    def __init__(
            self,
            api_key,
            platform_routing: str ='NA1',
            region_routing:str = 'AMERICAS'):

        self._transport = LoLAPITransport(
            api_key=api_key,
            platform_routing=platform_routing,
            region_routing=region_routing
        )
        self.summoner = LoLSummonerClient(self._transport)
        self.match = LoLMatchClient(self._transport)
        self.data_dragon = DataDragonClient(self._transport)
