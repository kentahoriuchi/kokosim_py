from baseball.entity.player import Player
from baseball.entity.team import Team
from random import gauss
from baseball.scripts.create_name import create_player_name
from baseball.scripts.create_name import create_team_name


# 平均の能力を持つチームを生成
def normal_team_generate() -> Team:
    team = Team()
    player_list = []
    for _ in range(9):
        player = Player()
        player.batter\
            .set_contact(50)\
            .set_power(50)\
            .set_run(50)\
            .set_defence(50)\
            .set_throw(50)
        player_list.append(player)
    pitcher = Player()
    pitcher.pitcher\
        .set_speed(50)\
        .set_control(50)\
        .set_henka(50)\
        .set_max_stamina(50)
    team.set_players(player_list)
    team.set_pitcher(pitcher)
    return team


# ガウス分布に沿うランダムな能力を持つチームを生成
def gauss_random_team_generate() -> Team:
    ave = 50  # 平均
    sd = 20  # 標準偏差
    team = Team()
    team.set_name(create_team_name())
    player_list = []
    for _ in range(9):
        player = Player().set_name(create_player_name())
        player.batter\
            .set_contact(validate_spec(int(gauss(ave, sd))))\
            .set_power(validate_spec(int(gauss(ave, sd))))\
            .set_run(validate_spec(int(gauss(ave, sd))))\
            .set_defence(validate_spec(int(gauss(ave, sd))))\
            .set_throw(validate_spec(int(gauss(ave, sd))))
        player_list.append(player)

    pitcher = Player().set_name(create_player_name())
    pitcher.pitcher\
        .set_speed(validate_spec(int(gauss(ave, sd))))\
        .set_control(validate_spec(int(gauss(ave, sd))))\
        .set_henka(validate_spec(int(gauss(ave, sd))))\
        .set_max_stamina(validate_spec(int(gauss(ave, sd))))
    player_list = optimize_player_list_neo(player_list)
    team.set_players(player_list)
    team.set_pitcher(pitcher)
    return team


def validate_spec(num):
    if num <= 0:
        return 1
    elif num >= 100:
        return 100
    else:
        return num


# 打順の最適化(どの順に強い選手を並べるか)
def optimize_player_list_neo(player_list: list[Player]):
    # どの打順に強い順で並べるか
    best_order = [4, 3, 1, 5, 2, 6, 7, 8, 9]
    stats = []
    for i in range(9):
        stat = player_list[i].batter.power + player_list[i].batter.contact
        stats.append(stat)
    best_player_list = [Player()] * 9
    for j in range(9):
        ind = stats.index(max(stats))
        stats[ind] = 0
        best_player_list[best_order[j]-1] = player_list[ind]

    return best_player_list

