from entity.pitcher import Pitcher
from entity.batter import Batter
from entity.team import Team


def normal_team_generate():
    first_team = Team()
    second_team = Team()
    player_list = []
    for _ in range(9):
        batter = Batter.ButterBuilder().name("バッター").contact(50).power(50).run(50).defence(50).throw(50).build()
        player_list.append(batter)
    pitcher = Pitcher.PitcherBuilder().name("ピッチャー").speed(50).control(50).henka(50).stamina(50).build()
    first_team.set_players(player_list)
    first_team.set_pitcher(pitcher)
    second_team.set_players(player_list)
    second_team.set_pitcher(pitcher)
    return first_team, second_team
