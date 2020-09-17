
from riotwatcher import LolWatcher, ApiError
import os

lol_watcher = LolWatcher(os.environ['RIOT_API'])

my_region = 'na1'
versions = lol_watcher.data_dragon.versions_for_region(my_region)
champions_version = versions['n']['champion']
current_champ_list = lol_watcher.data_dragon.champions(champions_version)





def bans(region,player):
    ban_list = []
    champs = lol_watcher.champion_mastery.by_summoner(region, player['id'])
    for i in range (0,3):
        ban_list.append(champs[i]['championId'])
    return (ban_list)


while True:
    print("Look up a summoner: ")
    summoner_name = input()
    player = lol_watcher.summoner.by_name(my_region, summoner_name)
    ban_list = (bans(my_region, player))

    print("Ban these champs:")

    for champion in (current_champ_list['data']):
        if int(current_champ_list['data'][champion]['key']) in ban_list:
            ban_list[ban_list.index(int(current_champ_list['data'][champion]['key']))] = current_champ_list['data'][champion]['name']


    for champ in ban_list:
        print(champ)


