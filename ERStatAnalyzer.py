import os
import json
import time

classDict = {1: "Diver", #Jackie
             2: "Backline", #Aya
             3: "Frontline", #Fiora
             4: "Frontline", #Magnus
             5: "Backline", #Zahir
             6: "Backline", #Nadine
             7: "Frontline", #Hyunwoo
             8: "Backline", #Hart
             9: "Backline", #Isol
             10: "Frontline", #Li Dailin
             11: "Frontline", #Yuki
             12: "Backline", #Hyejin
             13: "Tank", #Xiukai
             14: "Frontline", #Chiara
             15: "Backline", #Sissela
             16: "Diver", #Silvia
             17: "Backline", #Adriana
             18: "Diver", #Shoichi
             19: "Backline", #Emma
             20: "Tank", #Lenox
             21: "Backline", #Rozzi
             22: "Frontline", #Luke
             23: "Diver", #Cathy
             24: "Backline", #Adela
             25: "Backline", #Bernice
             26: "Frontline", #Barbara
             27: "Frontline", #Alex
             28: "Frontline", #Sua
             29: "Frontline", #Leon
             30: "Tank", #Eleven
             31: "Backline", #Rio
             32: "Backline", #William
             33: "Frontline", #Nicky
             34: "Backline", #Nathapon
             35: "Frontline", #Jan
             36: "Backline", #Eva
             37: "Diver", #Daniel
             38: "Backline", #Jenny
             39: "Frontline", #Camilo
             40: "Backline", #Chloe
             41: "Support", #Johann
             42: "Diver", #Bianca
             43: "Backline", #Celine
             44: "Frontline", #Echion
             45: "Tank", #Mai
             46: "Frontline", #Aiden
             47: "Frontline", #Laura
             48: "Backline", #Tia
             49: "Frontline", #Felix
             50: "Frontline", #Elena
             51: "Backline", #Priya
             52: "Backline", #Adina
             53: "Frontline", #Markus
             54: "Backline", #Karla
             55: "Tank", #Estelle
             56: "Frontline", #Piolo
             57: "Backline", #Martina
             58: "Backline", #Haze
             59: "Frontline", #Isaac
             60: "Frontline", #Tazia
             61: "Backline", #Irem
             62: "Backline", #Theodore
             63: "Frontline", #Ly Anh
             64: "Frontline", #Vanya
             65: "Frontline", #DeMa
             66: "Backline", #Arda
             67: "Frontline", #Abigail
             68: "Tank", #Alonso
             69: "Support", #Leni
             70: "Backline", #Tsubame
             71: "Frontline", #Kenneth
             71: "Frontline", #Kenneth
             72: "Backline", #Katja
             73: "Support", #Charlotte
             74: "Frontline", #Darko
             }

def organizeTeams(data):
    teams = dict()
    
    for player in data:
        if player['teamNumber'] in teams:
            teams[player['teamNumber']].append(player)
        else:
            teams[player['teamNumber']] = [player]
    
    return teams
    
def hasCamilo(team):
    if team[0]['characterNum'] == 39 or team[1]['characterNum'] == 39 or team[2]['characterNum'] == 39:
        return True
    return False
    
def hasCharlotte(team):
    if team[0]['characterNum'] == 73 or team[1]['characterNum'] == 73 or team[2]['characterNum'] == 73:
        return True
    return False
    
def hasSupport(team):
    if classDict[team[0]['characterNum']] == "Support" or classDict[team[1]['characterNum']] == "Support" or classDict[team[2]['characterNum']] == "Support":
        return True
    return False
    
def hasTank(team):
    if classDict[team[0]['characterNum']] == "Tank" or classDict[team[1]['characterNum']] == "Tank" or classDict[team[2]['characterNum']] == "Tank":
        return True
    return False
    
def hasBackline(team):
    if classDict[team[0]['characterNum']] == "Backline" or classDict[team[1]['characterNum']] == "Backline" or classDict[team[2]['characterNum']] == "Backline":
        return True
    return False
    
def hasSupportAdjacent(team):
    if classDict[team[0]['characterNum']] == "Support" or classDict[team[1]['characterNum']] == "Support" or classDict[team[2]['characterNum']] == "Support":
        return True
    if team[0]['characterNum'] == 51 or team[1]['characterNum'] == 51 or team[2]['characterNum'] == 51:
        return True
    if team[0]['characterNum'] == 52 or team[1]['characterNum'] == 52 or team[2]['characterNum'] == 52:
        return True
    if team[0]['characterNum'] == 62 or team[1]['characterNum'] == 62 or team[2]['characterNum'] == 62:
        return True
    return False

def onlyFrontline(team):
    if ((classDict[team[0]['characterNum']] == "Frontline" or classDict[team[0]['characterNum']] == "Tank" or classDict[team[0]['characterNum']] == "Diver") and
       (classDict[team[1]['characterNum']] == "Frontline" or classDict[team[1]['characterNum']] == "Tank" or classDict[team[1]['characterNum']] == "Diver") and
       (classDict[team[2]['characterNum']] == "Frontline" or classDict[team[2]['characterNum']] == "Tank" or classDict[team[2]['characterNum']] == "Diver")):
       return True
    return False

def doubleBackline(team):
    count = 0
    if classDict[team[0]['characterNum']] == "Backline":
        count += 1

    if classDict[team[1]['characterNum']] == "Backline":
        count += 1
    
    if classDict[team[2]['characterNum']] == "Backline":
        count += 1
    
    return count == 2

def doubleFrontline(team):
    count = 0
    if classDict[team[0]['characterNum']] == "Frontline":
        count += 1

    if classDict[team[1]['characterNum']] == "Frontline":
        count += 1
    
    if classDict[team[2]['characterNum']] == "Frontline":
        count += 1
    
    return count == 2
    
def camiloWithSupport(team):
    if hasCamilo(team) and hasSupport(team):
        return True
    return False
    
def camiloWithTank(team):
    return hasTank(team) and hasCamilo(team)
 
def doubleFrontlineBackline(team):
    return doubleFrontline(team) and hasBackline(team)
    
def getStatsWithConditions(teamCondition, playerCondition):
    stats = list()

    for file in os.listdir("./ERGameData"):
        f = open(f"ERGameData/{file}", "r", encoding="utf-8");
        data = json.load(f)
        
        
        
        teams = organizeTeams(data['userGames'])
        for teamNum in teams:
            if teamCondition(teams[teamNum]):
                for player in teams[teamNum]:
                    if playerCondition(player):
                        stats.append(player)

    return stats

def averageStatValue(stats, fieldName):
    if len(stats) == 0:
        return 0
        
    total = 0
    count = 0
    
    for player in stats:
        total += player[fieldName]
        count += 1
    
    return total / count

#other relevant conditions include "versionMajor", "versionMinor", "serverName"
def playerConditions(player): #character is camilo, is ranked, and is season 4
    return player['characterNum'] == 39 and player['matchingMode'] == 3 and player['seasonId'] == 25

stats = getStatsWithConditions(doubleFrontlineBackline, playerConditions)

print("Total number of games meeting criteria: ", len(stats))
print("Average game rank: ", averageStatValue(stats, "gameRank"))
print("Average total MMR gain: ", averageStatValue(stats, "mmrGainInGame"))
averageKills = averageStatValue(stats, "teamElimination")
averageBZDowns = averageStatValue(stats, "teamBattleZoneDown")
averageDowns = averageStatValue(stats, "teamElimination")
print("Average team kills: ", averageKills + averageBZDowns + averageDowns)
print("Average team elims: ", averageKills)
print("Average team downs: ", averageDowns)
print("Average team BZ downs: ", averageBZDowns)
print("Average deaths: ", averageStatValue(stats, "playerDeaths"))
print("Average healing: ", averageStatValue(stats, "healAmount"))
print("Average shielding: ", averageStatValue(stats, "protectAbsorb"))
print("Average damage: ", averageStatValue(stats, "damageToPlayer"))
print("Average damage taken: ", averageStatValue(stats, "damageFromPlayer"))