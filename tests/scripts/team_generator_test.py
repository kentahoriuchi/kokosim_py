import pytest
from baseball.scripts.team_generator import normal_team_generate, gauss_random_team_generate

def test_正常にnormal_team_generateが動作する():
    team = normal_team_generate()
    assert len(team.player_list) == 9
    test_player = team.player_list[0]
    assert test_player.batter.contact == 50
    test_pitcher = team.pitcher
    assert test_pitcher.pitcher.speed == 50

def test_正常にgauss_random_team_generateが動作する():
    team = gauss_random_team_generate()
    assert len(team.player_list) == 9
    test_player = team.player_list[0]
    assert test_player.batter.contact >= 1
    assert test_player.batter.contact <= 100
    test_pitcher = team.pitcher
    assert test_pitcher.pitcher.speed >= 1
    assert test_pitcher.pitcher.speed <= 100

def test_正常にoptimize_player_list_neoが動作する():
    # gauss_random_team_generate内に組み込まれているためこちらで検証する
    team = gauss_random_team_generate()
    assert team.player_list[3].batter.contact + team.player_list[3].batter.power \
           >= team.player_list[2].batter.contact + team.player_list[2].batter.power
    assert team.player_list[7].batter.contact + team.player_list[7].batter.power \
           >= team.player_list[8].batter.contact + team.player_list[8].batter.power
