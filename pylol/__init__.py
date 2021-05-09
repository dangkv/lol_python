from pylol.transport import LoLAPITransport
from pylol.LoLSummonerClient import LoLSummonerClient


class PyLoL:
    def __init__(self, api_key, region='NA1'):
        self._transport = LoLAPITransport(api_key, region)
        self.summoner = LoLSummonerClient(self._transport)

# Match
