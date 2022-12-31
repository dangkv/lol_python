# lol_python - League of Legends Python API WRAPPER
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A Python API Wrapper for Riot League of Legends API Endpoints.

More Endpoints coming soon... :metal:

# :dart: Getting Started
1. Create a Riot development API key [here](https://developer.riotgames.com/)
2. Import lol_python into your script
3. Initialize the lol_python class using the API key in step 1
4. Enjoy.

# :spiral_notepad: Example

```python
from lol_python import lol_python

api_key = 'RIOT_API_KEY'

# Instantiate lol_python class
lol = lol_python(api_key=api_key)

# Get IDs using Summoner Name
ids = lol.summoner.ids('Summoner Name')

# Get list of match IDs
match_list = lol.match.list('Summoner PUUID')

# Get Match summary
match_summary = lol.match.summary('Match ID')

# Get detailed match events
match_timeline = lol.match.timeline('Match ID')
```

# :-1: Rate Limits
- 20 requests every 1 seconds(s)
- 100 requests every 2 minutes(s)
