import pytest
from sqlalchemy.orm.exc import NoResultFound
from baseball.entity.player import Player
from baseball.repository.player import PlayerData, get_players_by_team
import baseball.repository.orm as orm


@pytest.fixture(scope='module', autouse=True)
def create_db():
    player = PlayerData()
    player.create_table()


@pytest.fixture(scope='function', autouse=True)
def db():
    # テーブル内初期化
    orm.delete_all(PlayerData)


def test_正しくプレイヤーが登録できる(db):
    player = Player()
    expected_name = player.name
    expected_contact = player.batter.contact
    expected_pitcher_runs = player.pitcher.pitcher_stats.runs

    player_data = player.convert_to_dataclass()
    target_id = 1
    player_data.id = target_id
    orm.insert(player_data)

    actual_player: PlayerData = orm.read(PlayerData, target_id)
    assert actual_player.name == expected_name
    assert actual_player.contact == expected_contact
    assert actual_player.pitcher_runs == expected_pitcher_runs

def test_正しくプレイヤー情報が更新できる(db):
    player = Player()
    expected_contact = player.batter.contact
    expected_pitcher_runs = player.pitcher.pitcher_stats.runs

    player_data = player.convert_to_dataclass()
    target_id = 1
    player_data.id = target_id
    orm.insert(player_data)

    update_name = "updated"
    player_data.name = update_name
    orm.update(PlayerData, player_data, target_id)

    actual_player: PlayerData = orm.read(PlayerData, target_id)
    assert actual_player.name == update_name
    assert actual_player.contact == expected_contact
    assert actual_player.pitcher_runs == expected_pitcher_runs

def test_正しくプレイヤーを削除できる(db):
    player = Player()

    player_data = player.convert_to_dataclass()
    target_id = 1
    player_data.id = target_id
    orm.insert(player_data)

    orm.delete(PlayerData, target_id)
    with pytest.raises(NoResultFound) as e:
        actual_player: PlayerData = orm.read(PlayerData, target_id)
    assert str(e.value) == "No row was found when one was required"

def test_チーム指定で選手を読み込める(db):
    player1 = Player()
    player2 = Player()
    target_team = "test"
    player1.school = target_team
    player2.school = target_team

    player_data_list = [player1.convert_to_dataclass(), player2.convert_to_dataclass()]
    orm.insert_all(player_data_list)

    actual_player_list = get_players_by_team(target_team)
    assert len(list(actual_player_list)) == 2
