import json

import pyperclip
from pylol import PyLoL

API_KEY = "RGAPI-fdf3075b-3fc7-43e6-94a2-ebdb1592afe2"


lol = PyLoL(api_key=API_KEY)
ids = lol.summoner.ids('zeratul1')


puuid = ids['puuid']


match_list = lol.match.list(puuid)
match_1 = match_list[0]

match_summary = lol.match.summary(match_1)
match_timeline = lol.match.timeline(match_1)
# pyperclip.copy(lol.data_dragon.champions())

print(json.dumps(lol.data_dragon.champions()))
