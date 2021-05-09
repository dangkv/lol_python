import os
from dotenv import load_dotenv, find_dotenv
from pylol import PyLoL
import logging

load_dotenv(find_dotenv())

api_key = os.getenv('RIOT_API_KEY')

lol = PyLoL(api_key=api_key)


print(lol.summoner.get_details('zeratul1'))
