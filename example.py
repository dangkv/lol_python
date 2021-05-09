import os
from dotenv import load_dotenv, find_dotenv
from pylol import PyLoL

load_dotenv(find_dotenv())

api_key = os.getenv('RIOT_API_KEY')

lol = PyLoL(api_key=api_key)
account = lol.summoner.ids('justkiddoh')
puuid = account['puuid']
# a_match = lol.match.list(puuid)[0]
# match_summary = lol.match.summary(a_match)
# match_timeline = lol.match.timeline(a_match)
print(account)
