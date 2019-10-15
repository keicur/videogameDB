import json
import datetime
from create_db_games import game_id
from igdb_api_python.igdb import igdb
igdb = igdb("80b0f05c0e4a20c67558580bb1f0161d")



all_game_engines = { }

ids_array = []

for i in range (100):
    ids_array.append(game_id[i])

result = igdb.games({
    'ids': [2033,8500],
    'fields': ['name','game_engines.name','game_engines.games','game_engines.platforms','game_engines.created_at','game_engines.url'],
    'expand': 'game_engines'
})

for game in result.body:
    for game_engine in game['game_engines']:
        if str(game_engine["id"]) in all_game_engines:
            all_game_engines[str(game_engine["id"])]["game"] = all_game_engines[str(game["id"])]["game"] + "," + game['name']
        else:
            name = game_engine["name"] if "name" in game_engine else None
            games = game_engine["games"] if "games" in game_engine else None
            platforms = game_engine["platforms"] if "platforms" in game_engine else None
            created_at = game_engine["created_at"] if "created_at" in game_engine else None
            url = game_engine["url"] if "url" in game_engine else None

            all_game_engines[str(game_engine["id"])] = \
                {"id" : str(game_engine["id"]),
                 "name": name,
                 "games": games,
                 "platforms": platforms,
                 "created_at": created_at,
                 "url": url
                 }

saved_games = []

for g in all_game_engines.values():
    saved_games.append(g)

with open('engines.json', 'w') as fp:
    json.dump(saved_games, fp, indent=2)
