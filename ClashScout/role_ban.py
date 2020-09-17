
from riotwatcher import LolWatcher, ApiError
import os

lol_watcher = LolWatcher(os.environ['RIOT_API'])

my_region = 'na1'
versions = lol_watcher.data_dragon.versions_for_region(my_region)
champions_version = versions['n']['champion']
current_champ_list = lol_watcher.data_dragon.champions(champions_version)


def collectChamps(matches, role):
    champion_tally = {}
    if role.upper() == "MID" or role.upper() == "MIDDLE":
        for i in range(len(matches)):
            if matches[i]['lane'] == 'MID':
                if matches[i]['champion'] in champion_tally:
                    champion_tally[matches[i]['champion']] += 1
                else: champion_tally[matches[i]['champion']] = 1

    if role.upper() == "JUNG" or role.upper() == "JUNGLE":
        for i in range(len(matches)):
            if matches[i]['lane'] == 'JUNGLE':
                if matches[i]['champion'] in champion_tally:
                    champion_tally[matches[i]['champion']] += 1
                else: champion_tally[matches[i]['champion']] = 1

    if role.upper() == "BOT" or role.upper() == "ADC":
        for i in range(len(matches)):
            if matches[i]['role'] == 'DUO_CARRY':
                if matches[i]['champion'] in champion_tally:
                    champion_tally[matches[i]['champion']] += 1
                else: champion_tally[matches[i]['champion']] = 1

    if role.upper() == "SUP" or role.upper() == "SUPPORT":
        for i in range(len(matches)):
            if matches[i]['role'] == 'DUO_SUPPORT':
                if matches[i]['champion'] in champion_tally:
                    champion_tally[matches[i]['champion']] += 1
                else: champion_tally[matches[i]['champion']] = 1


    if role.upper() == "TOP" or role.upper() == "TOP LANE":
        for i in range(len(matches)):
            if matches[i]['lane'] == 'TOP':
                if matches[i]['champion'] in champion_tally:
                    champion_tally[matches[i]['champion']] += 1
                else: champion_tally[matches[i]['champion']] = 1



    return champion_tally



def bans(region,player, role, current_champ_list):
    matches = lol_watcher.match.matchlist_by_account(region, player['accountId'], {420, 700, 440})['matches']
    champion_tally = collectChamps(matches, role)
    ban_list = []
    for i in range(5):
        if champion_tally:
            current_ban = max(champion_tally, key=lambda k: champion_tally[k])
            champion_tally.pop(current_ban, None)
            ban_list.append(current_ban)

    for champion in (current_champ_list['data']):
        if int(current_champ_list['data'][champion]['key']) in ban_list:
            ban_list[ban_list.index(int(current_champ_list['data'][champion]['key']))] = current_champ_list['data'][champion]['name']
    return (ban_list)






while True:
    print("Look up a summoner: ")
    summoner_name = input()
    print("What role are they playing:")
    role = input()

    player = lol_watcher.summoner.by_name(my_region, summoner_name)
    ban_list = (bans(my_region, player, role, current_champ_list))

    print("Ban these champs:")

    for champ in ban_list:
        print(champ)


