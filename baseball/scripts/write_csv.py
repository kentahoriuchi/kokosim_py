from baseball.entity.team import Team
from baseball.entity.player import Player
import pandas as pd
import os


def write_csv_team(team: Team):
    folder_path = f'resource/' + team.name
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    batter_index = []
    batter_data = []
    for i in range(9):
        batter: Player = team.player_list[i]
        player_ability = {
            "grade": str(int(batter.grade)),
            "contact": batter.batter.contact,
            "power": batter.batter.power,
            "run": batter.batter.run,
            "defence": batter.batter.defence,
            "throw": batter.batter.throw
        }
        batter_stats = batter.batter.batter_stats
        player_stats = {
            "batter_box_count": batter_stats.batter_box_count,
            "average": batter_stats.average(),
            "homerun": batter_stats.homerun_count,
            "runs": batter_stats.runs,
            "strikeout": batter_stats.strikeout_count,
            "fourball": batter_stats.fourball_count
        }
        player_ability.update(player_stats)
        batter_index.append(batter.name)
        batter_data.append(player_ability)

    batter_df = pd.DataFrame(
        data=batter_data,
        index=batter_index
    )

    batter_df.to_csv(f'resource/%s/batter.csv' % team.name)

    pitcher_index = []
    pitcher_data = []
    for i in range(1):
        pitcher: Player = team.pitcher
        player_ability = {
            "grade": str(int(pitcher.grade)),
            "speed": str(pitcher.pitcher.speed//2 + 105) + "km/h",
            "control": pitcher.pitcher.control,
            "henka": pitcher.pitcher.henka,
            "stamina": pitcher.pitcher.stamina
        }
        pitcher_stats = pitcher.pitcher.pitcher_stats
        player_stats = {
            "inning": pitcher_stats.inning(),
            "era": pitcher_stats.era(),
            "strikeout": pitcher_stats.strikeout,
            "runs": pitcher_stats.runs,
            "fourball": pitcher_stats.fourball
        }
        player_ability.update(player_stats)
        pitcher_index.append(pitcher.name)
        pitcher_data.append(player_ability)

    pitcher_df = pd.DataFrame(
        data=pitcher_data,
        index=pitcher_index
    )

    pitcher_df.to_csv(f'resource/%s/pitcher.csv' % team.name)
