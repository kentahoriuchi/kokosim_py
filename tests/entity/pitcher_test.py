import pytest
from baseball.entity.pitcher import Pitcher

def test_正常にピッチャーを作製できる():
    pitcher = Pitcher()\
        .set_speed(50)\
        .set_stamina(50)\
        .set_control(50)\
        .set_henka(50)
    assert pitcher.speed == 50
    assert pitcher.stamina == 50
    assert pitcher.control == 50
    assert pitcher.henka == 50

def test_初期値のピッチャーを作製できる():
    pitcher = Pitcher()
    assert pitcher.speed == 1
    assert pitcher.stamina == 1
    assert pitcher.control == 1
    assert pitcher.henka == 1


def test_指定したステータスの値が低い():
    with pytest.raises(ValueError) as e:
        pitcher = Pitcher() \
            .set_speed(0) \
            .set_stamina(50) \
            .set_control(50) \
            .set_henka(50)
    assert str(e.value) == "invalid speed value"

def test_指定したステータスの値が高い():
    with pytest.raises(ValueError) as e:
        pitcher = Pitcher() \
            .set_speed(50) \
            .set_stamina(101) \
            .set_control(50) \
            .set_henka(50)
    assert str(e.value) == "invalid stamina value"
