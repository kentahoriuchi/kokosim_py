from entity.pitcher import Pitcher
from entity.batter import Batter
from entity.team import Team
from game import Game
from random import randint
from random import shuffle
from scripts.create_name import create_player_name
from scripts.create_name import create_team_name


def normal_team_generate() -> Team:
    team = Team()
    player_list = []
    for _ in range(9):
        batter = Batter.ButterBuilder()\
            .name("バッター")\
            .contact(50)\
            .power(50)\
            .run(50)\
            .defence(50)\
            .throw(50)\
            .build()
        player_list.append(batter)
    pitcher = Pitcher.PitcherBuilder()\
        .name("ピッチャー")\
        .speed(50)\
        .control(50)\
        .henka(50)\
        .stamina(50)\
        .build()
    team.set_players(player_list)
    team.set_pitcher(pitcher)
    return team


def random_team_generate() -> Team:
    team = Team()
    team.set_name(create_team_name())
    player_list = []
    for _ in range(9):
        batter = Batter.ButterBuilder()\
            .name(create_player_name())\
            .contact(randint(1, 100))\
            .power(randint(1, 100))\
            .run(randint(1, 100))\
            .defence(randint(1, 100))\
            .throw(randint(1, 100))\
            .build()
        player_list.append(batter)
    pitcher = Pitcher.PitcherBuilder()\
        .name(create_player_name())\
        .speed(randint(1, 100))\
        .control(randint(1, 100))\
        .henka(randint(1, 100))\
        .stamina(randint(1, 100))\
        .build()
    # player_list = optimize_player_list(player_list)
    team.set_players(player_list)
    team.set_pitcher(pitcher)
    return team


def optimize_player_list(player_list):
    best_order = player_list
    best_score = 0
    normal_team = normal_team_generate()
    for _ in range(100):
        print(best_order)
        print(best_score)
        candidate_list = best_order
        shuffle(candidate_list)
        candidate_team = Team()
        candidate_team.set_players(candidate_list)
        pitcher = Pitcher.PitcherBuilder() \
            .name("ピッチャー") \
            .speed(50) \
            .control(50) \
            .henka(50) \
            .stamina(50) \
            .build()
        candidate_team.set_pitcher(pitcher)
        score = 0
        for _ in range(30):
            game = Game(candidate_team, normal_team, False)
            game.start_game()
            tmp_score, _ = game.get_score()
            score += tmp_score
        if score > best_score:
            best_order = candidate_list
            best_score = score

    return best_order

