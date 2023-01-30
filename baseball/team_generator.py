from entity.pitcher import Pitcher
from entity.batter import Batter
from entity.team import Team
from random import randint
from scripts.create_name import create


def normal_team_generate() -> (Team, Team):
    first_team = Team()
    second_team = Team()
    player_list1 = []
    player_list2 = []
    for _ in range(9):
        batter = Batter.ButterBuilder()\
            .name("バッター")\
            .contact(50)\
            .power(50)\
            .run(50)\
            .defence(50)\
            .throw(50)\
            .build()
        player_list1.append(batter)
    pitcher1 = Pitcher.PitcherBuilder()\
        .name("ピッチャー")\
        .speed(50)\
        .control(50)\
        .henka(50)\
        .stamina(50)\
        .build()
    first_team.set_players(player_list1)
    first_team.set_pitcher(pitcher1)
    for _ in range(9):
        batter = Batter.ButterBuilder().name("バッター").contact(50).power(50).run(50).defence(50).throw(50).build()
        player_list2.append(batter)
    pitcher2 = Pitcher.PitcherBuilder().name("ピッチャー").speed(50).control(50).henka(50).stamina(50).build()
    second_team.set_players(player_list2)
    second_team.set_pitcher(pitcher2)
    return first_team, second_team

def ramdom_team_generate() -> (Team, Team):
    first_team = Team()
    second_team = Team()
    player_list1 = []
    player_list2 = []
    for _ in range(9):
        batter = Batter.ButterBuilder()\
            .name(create())\
            .contact(randint(1, 100))\
            .power(randint(1, 100))\
            .run(randint(1, 100))\
            .defence(randint(1, 100))\
            .throw(randint(1, 100))\
            .build()
        player_list1.append(batter)
    pitcher1 = Pitcher.PitcherBuilder()\
        .name(create())\
        .speed(randint(1, 100))\
        .control(randint(1, 100))\
        .henka(randint(1, 100))\
        .stamina(randint(1, 100))\
        .build()
    first_team.set_players(player_list1)
    first_team.set_pitcher(pitcher1)
    for _ in range(9):
        batter = Batter.ButterBuilder() \
            .name(create()) \
            .contact(randint(1, 100)) \
            .power(randint(1, 100)) \
            .run(randint(1, 100)) \
            .defence(randint(1, 100)) \
            .throw(randint(1, 100)) \
            .build()
        player_list2.append(batter)
    pitcher2 = Pitcher.PitcherBuilder() \
        .name(create()) \
        .speed(randint(1, 100)) \
        .control(randint(1, 100)) \
        .henka(randint(1, 100)) \
        .stamina(randint(1, 100)) \
        .build()
    second_team.set_players(player_list2)
    second_team.set_pitcher(pitcher2)
    return first_team, second_team
