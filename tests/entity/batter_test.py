import pytest
from baseball.entity.batter import Batter, BatterStatus

def test_正常にバッターを作製できる():
    batter = Batter()\
        .set_contact(50)\
        .set_power(50)\
        .set_run(50)\
        .set_defence(50)\
        .set_throw(50)\
        .set_batting_eye(50)\
        .set_c_lead(50)
    assert batter.contact == 50
    assert batter.power == 50
    assert batter.run == 50
    assert batter.defence == 50
    assert batter.throw == 50
    assert batter.batting_eye == 50
    assert batter.c_lead == 50

def test_初期値のバッターを作製できる():
    batter = Batter()
    assert batter.contact == 1
    assert batter.power == 1
    assert batter.run == 1
    assert batter.defence == 1
    assert batter.throw == 1

def test_指定したステータスの値が低い():
    with pytest.raises(ValueError) as e:
        batter = Batter() \
            .set_contact(0) \
            .set_power(50) \
            .set_run(50) \
            .set_defence(50) \
            .set_throw(50)
    assert str(e.value) == "invalid contact value"

def test_指定したステータスの値が高い():
    with pytest.raises(ValueError) as e:
        batter = Batter() \
            .set_contact(50) \
            .set_power(101) \
            .set_run(50) \
            .set_defence(50) \
            .set_throw(50)
    assert str(e.value) == "invalid power value"


@pytest.fixture(scope='function', autouse=True)
def preset_batter() -> Batter:
    batter = Batter() \
        .set_contact(50) \
        .set_power(50) \
        .set_run(50) \
        .set_defence(50) \
        .set_throw(50)
    # 最初から経験値を入れておく
    batter.batter_ex_point.contact = 50
    return batter

def test_経験値の値が増える(preset_batter):
    preset_batter.get_ex_point({BatterStatus.contact: 10, BatterStatus.power: 10})
    assert preset_batter.batter_ex_point.contact == 60
    assert preset_batter.batter_ex_point.power == 10
    assert preset_batter.contact == 50

def test_経験値によって能力値が上昇する(preset_batter):
    preset_batter.get_ex_point({BatterStatus.contact: 51, BatterStatus.defence: 200})
    assert preset_batter.batter_ex_point.contact == 1
    assert preset_batter.batter_ex_point.defence == 0
    assert preset_batter.contact == 51
    assert preset_batter.defence == 52

def test_経験値に不正なキーが混ざっている(preset_batter):
    with pytest.raises(ValueError) as e:
        preset_batter.get_ex_point({BatterStatus.contact: 51, "": 200})
    assert str(e.value) == "invalid key in batter ex_point dict"
