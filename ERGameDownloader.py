import requests
import json
import time
import os

key = "API_KEY_OMITTED" #api key would go here if you have one
headers = {
    "x-api-key": key
}

def playerCodeFromName(name):
    query = {"query": name}
    data = requests.get("https://open-api.bser.io/v1/user/nickname", headers = headers, params = query)
    
    return data.json()['user']['userNum']
    
def playerGamesQuery(playerCode, nextGame = None):
    data = None
    if nextGame == None:
        data = requests.get(f"https://open-api.bser.io/v1/user/games/{playerCode}", headers = headers)
    else:
        query = {"next": nextGame}
        data = requests.get(f"https://open-api.bser.io/v1/user/games/{playerCode}", headers = headers, params = query)
    
    return data.json()
    
def getAllPlayerGames(playerCode, maxGames):
    data = playerGamesQuery(playerCode)
    
    idList = list()
    
    while data["code"] == 200 and len(idList) < maxGames:
        for game in data['userGames']:
            idList.append(game["gameId"])
        
        time.sleep(1)
        print("Num games: ", len(idList))
        if "next" in data.keys():
            data = playerGamesQuery(playerCode, nextGame = data["next"])
        else:
            break
    
    return idList


playerCode = playerCodeFromName("EXAMPLE_PLAYER_NAME")
gamesList = getAllPlayerGames(playerCode, 180)

playerCode = playerCodeFromName("EXAMPLE_SECOND_PLAYER_NAME")
gamesList.extend(getAllPlayerGames(playerCode, 150))
#can continue this for as many players as wanted

count = 0

for game in gamesList:
    if os.path.isfile(f"ERGameData/{game}.json"):
        print("file exists")
        count+=1
        continue
    
    data = requests.get(f"https://open-api.bser.io/v1/games/{game}", headers = headers)
    
    time.sleep(1)

    f = open(f"ERGameData/{game}.json", "w", encoding="utf-8")

    f.write(str(json.dumps(data.json(), indent=4)))
    print(count)
    count+=1
