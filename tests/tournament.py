import pytest
import shutil
import time
from baseball.baseball_game import BaseballGame
from baseball.scripts.write_csv import write_csv_team
from baseball.tournament import Tournament


def test_トーナメントを実行():
    time_sta = time.time()

    tournament = Tournament(128)
    tournament.random_team_generator()
    # 時間計測終了
    time_end = time.time()
    # 経過時間（秒）
    tim = time_end - time_sta
    print(str(tim) + " 秒")
    win_team, best4 = tournament.tournament()
    for i in range(len(win_team.games)):
        win_game: BaseballGame = win_team.games[i]
        print(str(win_game.get_lose_team().name) + " " + "%d vs %d" % (win_game.first_score, win_game.second_score))
        print(win_game.first_score_list)
        print(win_game.second_score_list)
    shutil.rmtree('outputs')
    for i in range(4):
        write_csv_team(best4[i], "outputs")

    # 時間計測終了
    time_end = time.time()
    # 経過時間（秒）
    tim = time_end - time_sta
    print(str(tim) + " 秒")
