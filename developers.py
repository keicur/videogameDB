import json
import datetime

from igdb_api_python.igdb import igdb
igdb = igdb("579d910039823e6c538106046d6ad3a6")

with open('games.json') as f:
    games = json.load(f)
developer_list = []
for a_game in games:
    print(a_game['developers'])

    try:
        dev_id_list = a_game['developers']
        if dev_id_list != None:
            for id in dev_id_list:
                try:
                    dev = igdb.companies(int(id))
                    print('=============')
                    print(dev.body[0])
                    developer_list.append(dev.body[0])
                except IndexError:
                    continue
    except KeyError:
        continue
with open('developers.json', 'w') as fp:
    json.dump(developer_list, fp, indent=2)
