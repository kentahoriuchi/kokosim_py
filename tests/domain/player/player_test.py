from baseball.domain.player.player import Player, Grade

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

def test_DB格納用のentityに変換できる():
    player = Player()\
        .set_name("テスト")\
        .set_school("テスト高校")
    player.batter\
        .set_contact(50)\
        .set_power(50)
    player.batter.batter_ex_point.throw = 10
    player.pitcher\
        .set_max_stamina(50)\
        .set_control(50)
    player.pitcher.add_pitch_types("スライダー", 50)
    player.pitcher.pitcher_ex_point.speed = 20

    player_db = player.convert_to_dataclass()
    player_converted = player_db.convert_to_entity()

    assert player.name == player_converted.name
    assert player.school == player_converted.school
    assert player.batter.contact == player_converted.batter.contact
    assert player.batter.power == player_converted.batter.power
    assert player.batter.batter_ex_point.throw == player_converted.batter.batter_ex_point.throw
    assert player.pitcher.max_stamina == player_converted.pitcher.max_stamina
    assert player.pitcher.control == player_converted.pitcher.control
    assert player.pitcher.pitch_types == player_converted.pitcher.pitch_types
    assert player.pitcher.pitcher_ex_point.speed == player_converted.pitcher.pitcher_ex_point.speed
