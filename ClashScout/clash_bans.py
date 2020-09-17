
from riotwatcher import LolWatcher, ApiError
import role_ban
import os

lol_watcher = LolWatcher(os.environ['RIOT_API'])

my_region = 'na1'
versions = lol_watcher.data_dragon.versions_for_region(my_region)
champions_version = versions['n']['champion']
current_champ_list = lol_watcher.data_dragon.champions(champions_version)


while True:
    print("Look up a summoner: ")
    summoner_name = input()
    summoner_id = lol_watcher.summoner.by_name(my_region, summoner_name)['id']
    team_id = lol_watcher.clash.by_summoner(my_region, summoner_id)['teamId']

    team = lol_watcher.clash.by_team(my_region, team_id)
    for player in team['players']:
        role = player['position']
        if role == "UTILITY":
            role = "SUPPORT"
        ban_list = role_ban.bans(my_region, player['summonerId'], role)
        print(ban_list)
