import pytest
from baseball.entity.player import Player, Grade

def test_正常にプレイヤーを作製できる():
    player = Player()\
        .set_name("テスト")\
        .set_school("テスト高校")
    assert player.name == "テスト"
    assert player.school == "テスト高校"
    assert player.grade == Grade.preattend

def test_バッター能力を設定できる():
    player = Player() \
        .set_name("テスト") \
        .set_school("テスト高校")
    player.batter\
        .set_contact(50)\
        .set_power(50)\
        .set_run(50)\
        .set_defence(50)\
        .set_throw(50)
    assert player.batter.contact == 50
    assert player.batter.power == 50
    assert player.batter.run == 50
    assert player.batter.defence == 50
    assert player.batter.throw == 50

def test_ピッチャー能力を設定できる():
    player = Player() \
        .set_name("テスト") \
        .set_school("テスト高校")
    player.pitcher \
        .set_speed(50) \
        .set_max_stamina(50) \
        .set_control(50) \
        .set_henka(50)
    assert player.pitcher.speed == 50
    assert player.pitcher.max_stamina == 50
    assert player.pitcher.control == 50
    assert player.pitcher.henka == 50

def test_学年の更新ができる():
    player = Player() \
        .set_name("テスト") \
        .set_school("テスト高校")
    assert player.grade == Grade.preattend
    player.update_grade()
    assert player.grade == Grade.first
    player.update_grade()
    assert player.grade == Grade.second
    player.update_grade()
    assert player.grade == Grade.third
    player.update_grade()
    assert player.grade == Grade.graduated
