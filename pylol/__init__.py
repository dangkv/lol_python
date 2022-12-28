from pylol.data_dragon_client import DataDragonClient
from pylol.match_client import LoLMatchClient
from pylol.summoner_client import LoLSummonerClient
from pylol.transport import LoLAPITransport




class PyLoL:
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
