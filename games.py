# begin
import json
import datetime
from igdb_api_python.igdb import igdb
igdb = igdb("80b0f05c0e4a20c67558580bb1f0161d")


#Platforms

'''
Wii:        5
PS3 :       9
360:        12
DS:         20
3DS:        37
PSP:        38
WiiU:       41
Vita:       46
PS4:        48
One:        49
Switch:     130
'''


all_games = { }

result = igdb.platforms({
    'ids': [48,49,130],
    'fields': ['name','games.name', 'games.aggregated_rating', 'games.first_release_date', 'games.cover', 'games.developers', 'games.game_engines'],
    'expand': 'games'
})

for platform in result.body:
    for game in platform['games']:
        if str(game["id"]) in all_games:
            all_games[str(game["id"])]["platform"] = all_games[str(game["id"])]["platform"] + "," + platform['name']
        else:
            name = game["name"] if "name" in game else None
            rating = game["aggregated_rating"] if "aggregated_rating" in game else None
            release = datetime.datetime.fromtimestamp(int(game["first_release_date"]/1000)).strftime('%Y-%m-%d') if "first_release_date" in game else None
            cover = game["cover"]["url"][2:].replace("t_thumb", "t_original") if "cover" in game else None
            developers = game["developers"] if "developers" in game else None
            engines = game["game_engines"] if "game_engines" in game else None


            all_games[str(game["id"])] = \
                {"id" : str(game["id"]),
                 "name": name,
                 "rating": rating,
                 "release": release,
                 "cover": cover,
                 "platform": platform['name'],
                 "developers" : developers,
                 "engines" : engines
                 }
                 

saved_games = []
game_id = []

for g in all_games.values():
    saved_games.append(g)

with open('games.json', 'w') as fp:
    json.dump(saved_games, fp, indent=2)
