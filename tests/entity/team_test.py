import pytest
from baseball.entity.team import Team
from baseball.entity.player import Player, Grade
from baseball.game import Game

def test_正常にチームが作成できる():
    team = Team()
    team.set_name("テストチーム")
    team.set_players([Player()] * 9)
    pitcher = Player()
    team.set_pitcher(pitcher)
    assert team.name == "テストチーム"
    assert len(team.player_list) == 9
    assert team.pitcher == pitcher

def test_プレイヤーが正しく追加できる():
    player = Player()\
        .set_name("テストプレイヤー")\
        .set_school("テスト高校")
    team = Team()
    team.add_player(player)
    assert len(team.player_list) == 1
    assert team.player_list[0] == player
    test_player: Player = team.player_list[0]
    assert test_player.name == "テストプレイヤー"
    assert test_player.school == "テスト高校"
    assert test_player.grade == Grade.preattend

def test_プレイヤーリストの長さが規定を超えている():
    team = Team()
    with pytest.raises(ValueError) as e:
        team.set_players([Player()] * 10)
    assert str(e.value) == "player list length must be less than 9"

def test_プレイヤーリストの長さを超えてプレイヤーを登録することはできない():
    team = Team()
    team.set_players([Player()] * 9)
    with pytest.raises(ValueError) as e:
        team.add_player(Player())
    assert str(e.value) == "cannot add player for player list over 9"

def test_試合の登録ができる():
    test_team = Team()
    opponent_team = Team()
    game = Game(test_team, opponent_team)
    test_team.add_game(game)
    assert len(test_team.games) == 1
    assert test_team.games[0] == game
