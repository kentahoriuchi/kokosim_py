import pytest
from baseball.entity.batter import Batter

def test_正常にバッターを作製できる():
    batter = Batter.ButterBuilder()\
        .name("テスト")\
        .contact(50)\
        .power(50)\
        .run(50)\
        .defence(50)\
        .throw(50).\
        build()
    assert batter.name == "テスト"
    assert batter.contact == 50
    assert batter.power == 50
    assert batter.run == 50
    assert batter.defence == 50
    assert batter.throw == 50

def test_指定したステータスの値が低い():
    with pytest.raises(ValueError) as e:
        batter = Batter.ButterBuilder()\
            .name("テスト")\
            .contact(0)\
            .power(50)\
            .run(50)\
            .defence(50)\
            .throw(50).\
            build()
    assert str(e.value) == "invalid contact value"

def test_指定したステータスの値が高い():
    with pytest.raises(ValueError) as e:
        batter = Batter.ButterBuilder()\
            .name("テスト")\
            .contact(50)\
            .power(101)\
            .run(50)\
            .defence(50)\
            .throw(50).\
            build()
    assert str(e.value) == "invalid power value"
