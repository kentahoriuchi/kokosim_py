from baseball.entity.team import Team
from baseball.entity.batter import Batter
from baseball.entity.pitcher import Pitcher
import pandas as pd
import os


def write_csv_team(team: Team):
    folder_path = f'resource/' + team.name
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    batter_index = []
    batter_data = []
    for i in range(9):
        batter: Batter = team.player_list[i]
        player_ability = {
            "contact": batter.contact,
            "power": batter.power,
            "run": batter.run,
            "defence": batter.defence,
            "throw": batter.throw
        }
        batter_stats = batter.batter_stats
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
        pitcher: Pitcher = team.pitcher
        player_ability = {
            "speed": str(pitcher.speed//2 + 110) + "km/h",
            "control": pitcher.control,
            "henka": pitcher.henka,
            "stamina": pitcher.stamina
        }
        pitcher_stats = pitcher.pitcher_stats
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
