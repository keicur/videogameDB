# beginning of create_db.py
import datetime
from models import db, Game, Engine, Developer
import psycopg2
import json, logging
from sqlalchemy.orm import sessionmaker


def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()
    return jsn


game_id = []

def game_dict():
    games = load_json('games.json')
    game_dict = {}
    for aGame in games['games']:
        game_dict[int(aGame['id'])]=aGame['name']
    return game_dict

def dev_dict():
    devs = load_json('developers.json')
    dev_dict = {}
    for aDev in devs['developers']:
        dev_dict[int(aDev['id'])]=aDev['name']
    return dev_dict

def engine_dict():
    engines = load_json('engines.json')
    engine_dict = {}
    for aEngine in engines['engines']:
        engine_dict[int(aEngine['id'])]=aEngine['name']
    return engine_dict

def country_dict():
    countries = load_json('iso3166-1.json')
    country_dict = {}
    for aCountry in countries['3166-1']:
        country_dict[int(aCountry['numeric'])]=aCountry['name']
    return country_dict




def create_engines():
    engines = load_json('engines.json')
    gameID_dict = game_dict()
    devID_dict = dev_dict()

    for oneEngine in engines['engines']:
        id = oneEngine['id']
        name = oneEngine['name'] if "name" in oneEngine else None

        #companies
        company_ids_temp =oneEngine['companies'] if "companies" in oneEngine else []
        company_ids = []
        for i in range(0,len(company_ids_temp)):
            if company_ids_temp[i] in devID_dict:
                company_ids.append(company_ids_temp[i])
        companies = []
        if(len(company_ids) == 0):
            companies.append('n/a')
        else:
            for i in range(0, len(company_ids)):
                if company_ids[i] in devID_dict:
                    companies.append(devID_dict[company_ids[i]])


        #platforms
        platform_ids_temp = oneEngine['platforms'] if "platforms" in oneEngine else []
        platform_id_list = [48, 49, 130]
        platform_ids = []

        for i in range(0,len(platform_ids_temp)):
            if platform_ids_temp[i] in platform_id_list:
                platform_ids.append(platform_ids_temp[i])

        platforms = []
        if (platform_ids == []):
            platforms.append('n/a')
        else:
            if 48 in platform_ids:
                platforms.append('Playstation 4')
            if 49 in platform_ids:
                platforms.append('Xbox One')
            if 130 in platform_ids:
                platforms.append('Nintendo Switch')

        #games
        game_ids_temp = oneEngine['games'] if "games" in oneEngine else None
        game_ids = []
        for i in range(0,len(game_ids_temp)):
            if game_ids_temp[i] in gameID_dict:
                game_ids.append(game_ids_temp[i])
        games = []
        for i in range(0, len(game_ids)):
            if game_ids[i] in gameID_dict:
                games.append(gameID_dict[game_ids[i]])


        logo = oneEngine['logo']['url'] if "logo" in oneEngine else None


        founding_temp = oneEngine['created_at'] if "created_at" in oneEngine else None
        #print(founding_temp)
        founding = datetime.datetime.fromtimestamp(founding_temp//1000).strftime('%Y-%m-%d')

        newEngine = Engine(id = id, name = name, games = games, game_ids = game_ids, companies = companies, company_ids = company_ids, platforms = platforms, logo = logo, founding = founding)

        db.session.merge(newEngine)
        db.session.commit()






def create_games():
    games = load_json('games.json')
    devID_dict = dev_dict()
    engineID_dict = engine_dict()

    for oneGame in games["games"]:
        id = oneGame['id'] if "id" in oneGame else None
        title = oneGame['name'] if "name" in oneGame else None
        rating = oneGame['rating'] if "rating" in oneGame else None
        release_date = oneGame['release'] if "release" in oneGame else None
        cover = oneGame['cover'] if "cover" in oneGame else None
        platforms = oneGame['platform'] if "platform" in oneGame else None

        #developer
        developer_ids = oneGame['developers'] if oneGame["developers"]!=None else []
        developers = []
        if(developer_ids == []):
            developers.append("n/a")
        else:
            for i in range(0, len(developer_ids)):
                if developer_ids[i] in devID_dict:
                    developers.append(devID_dict[developer_ids[i]])


        #engine
        engine_ids = oneGame['engines'] if oneGame["engines"]!=None else []
        engines = []
        if(engine_ids == []):
            engines.append("n/a")
        else:
            for i in range(0, len(engine_ids)):
                if engine_ids[i] in engineID_dict:
                    engines.append(engineID_dict[engine_ids[i]])



        newGame = Game(id = id, title = title, rating = rating, release_date = release_date, cover = cover, platforms = platforms, developers = developers, developer_ids = developer_ids, engines = engines, engine_ids = engine_ids)

        # After I create the game, I can then add it to my session.
        db.session.add(newGame)
        # commit the session to my DB.
        db.session.commit()


        game_id.append(id)



def create_developers():
    developers = load_json('developers.json')
    gameID_dict = game_dict()


    for oneDev in developers["developers"]:
        id = oneDev['id']
        name = oneDev['name']
        website = oneDev['website'] if "website" in oneDev else None
        logo = oneDev['logo']['url'] if "logo" in oneDev else None


        country_iso = oneDev['country'] if "country" in oneDev else None
        countryDict = country_dict()
        country = countryDict[country_iso] if country_iso!=None else None



        description= oneDev['description'] if 'description' in oneDev else None


        #games
        game_ids_temp = oneDev['developed'] if "developed" in oneDev else []
        game_ids = []
        for i in range(0,len(game_ids_temp)):
            if game_ids_temp[i] in gameID_dict:
                game_ids.append(game_ids_temp[i])
        games = []
        for i in range(0, len(game_ids)):
            if game_ids[i] in gameID_dict:
                games.append(gameID_dict[game_ids[i]])

        founding_temp = oneDev['created_at'] if "created_at" in oneDev else None
        #print(founding_temp)
        founding = datetime.datetime.fromtimestamp(founding_temp//1000).strftime('%Y-%m-%d')


        newDev = Developer(id = id, name = name, games = games, game_ids = game_ids, description = description, country = country, website = website, logo = logo, founding = founding)

        db.session.merge(newDev)
        db.session.commit()




if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    create_developers()
    create_engines()
    create_games()
