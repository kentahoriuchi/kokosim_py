import pytest
from baseball.domain.player.pitcher.pitcher import Pitcher, PitcherStatus

def test_正常にピッチャーを作製できる():
    pitcher = Pitcher()\
        .set_speed(50)\
        .set_max_stamina(50)\
        .set_control(50)\
        .set_henka(50)
    assert pitcher.speed == 50
    assert pitcher.max_stamina == 50
    assert pitcher.control == 50
    assert pitcher.henka == 50

def test_初期値のピッチャーを作製できる():
    pitcher = Pitcher()
    assert pitcher.speed == 1
    assert pitcher.max_stamina == 1
    assert pitcher.control == 1
    assert pitcher.henka == 1


def test_指定したステータスの値が低い():
    with pytest.raises(ValueError) as e:
        pitcher = Pitcher() \
            .set_speed(0) \
            .set_max_stamina(50) \
            .set_control(50) \
            .set_henka(50)
    assert str(e.value) == "invalid speed value"

def test_指定したステータスの値が高い():
    with pytest.raises(ValueError) as e:
        pitcher = Pitcher() \
            .set_speed(50) \
            .set_max_stamina(101) \
            .set_control(50) \
            .set_henka(50)
    assert str(e.value) == "invalid stamina value"


@pytest.fixture(scope='function', autouse=True)
def preset_pitcher() -> Pitcher:
    pitcher = Pitcher() \
        .set_speed(50) \
        .set_max_stamina(50) \
        .set_control(50) \
        .set_henka(50) \
        .add_pitch_types("スライダー", 50)
    # 最初から経験値を入れておく
    pitcher.pitcher_ex_point.speed = 50
    return pitcher

def test_経験値の値が増える(preset_pitcher):
    preset_pitcher.get_ex_point({PitcherStatus.speed: 10, PitcherStatus.max_stamina: 10})
    assert preset_pitcher.pitcher_ex_point.speed == 60
    assert preset_pitcher.pitcher_ex_point.max_stamina == 10

def test_経験値によって能力値が上昇する(preset_pitcher):
    preset_pitcher.get_ex_point({PitcherStatus.speed: 51, PitcherStatus.control: 200, "スライダー": 110})
    assert preset_pitcher.pitcher_ex_point.speed == 1
    assert preset_pitcher.pitcher_ex_point.control == 0
    assert preset_pitcher.pitcher_ex_point.pitch_types["スライダー"] == 10
    assert preset_pitcher.speed == 51
    assert preset_pitcher.control == 52
    assert preset_pitcher.pitch_types["スライダー"] == 51

def test_経験値に不正なキーが混ざっている(preset_pitcher):
    with pytest.raises(ValueError) as e:
        preset_pitcher.get_ex_point({PitcherStatus.speed: 10, "a": 10})
    assert str(e.value) == "invalid key in pitcher ex_point dict"
