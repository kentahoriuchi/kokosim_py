import pytest
from baseball.entity.pitcher import Pitcher

def test_正常にピッチャーを作製できる():
    pitcher = Pitcher.PitcherBuilder()\
        .name("テスト")\
        .speed(50)\
        .stamina(50)\
        .control(50)\
        .henka(50)\
        .build()
    assert pitcher.name == "テスト"
    assert pitcher.speed == 50
    assert pitcher.stamina == 50
    assert pitcher.control == 50
    assert pitcher.henka == 50

def test_指定したステータスの値が低い():
    with pytest.raises(ValueError) as e:
        pitcher = Pitcher.PitcherBuilder() \
            .name("テスト") \
            .speed(0) \
            .stamina(50) \
            .control(50) \
            .henka(50) \
            .build()
    assert str(e.value) == "invalid speed value"

def test_指定したステータスの値が高い():
    with pytest.raises(ValueError) as e:
        pitcher = Pitcher.PitcherBuilder() \
            .name("テスト") \
            .speed(50) \
            .stamina(101) \
            .control(50) \
            .henka(50) \
            .build()
    assert str(e.value) == "invalid stamina value"
