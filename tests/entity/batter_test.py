import pytest
from baseball.entity.batter import Batter

def test_正常にバッターを作製できる():
    batter = Batter()\
        .set_contact(50)\
        .set_power(50)\
        .set_run(50)\
        .set_defence(50)\
        .set_throw(50)
    assert batter.contact == 50
    assert batter.power == 50
    assert batter.run == 50
    assert batter.defence == 50
    assert batter.throw == 50

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
