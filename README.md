# PyLoL - League of Legends Python SDK
[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](http://www.opensource.org/licenses/MIT)

A Python client library to use the Riot LoL API

More Endpoints coming soon... :metal:

# :dart: Getting Started
1. Create a Riot development API key [here](https://developer.riotgames.com/)
2. Import PyLoL into your script
3. Initialize the PyLoL class using the API key in step 1
4. Enjoy.  

# :spiral_notepad: Example
```python
from pylol import PyLoL

api_key = 'RIOT_API_KEY'

# Instantiate PyLoL class 
lol = PyLoL(api_key=api_key)

# Get IDs using Summoner Name
ids = lol.summoner.ids('Your Summoner Name')

# Get list of match IDs
match_list = lol.match.list('Your Summoner Name')

# Get Match summary
match_summary = lol.match.summary('Match ID')

# Get detailed match events
match_timeline = lol.match.timeline('Match ID')
```

# :key: Dimensional Key
|Dimension|Type|Link|
|---|---|---|
|Champions | JSON |[Version 11.9.1](http://ddragon.leagueoflegends.com/cdn/11.9.1/data/en_US/champion.json) |

# :-1: Rate Limits
- 20 requests every 1 seconds(s)
- 100 requests every 2 minutes(s)