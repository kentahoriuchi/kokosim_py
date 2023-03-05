import json
from baseball.repository.mapper_setting import Base, Engine, Session
from sqlalchemy import Column, Integer, String


class PlayerData(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    grade = Column(Integer)
    school = Column(String(200), nullable=False)
    contact = Column(Integer)
    power = Column(Integer)
    run = Column(Integer)
    defence = Column(Integer)
    throw = Column(Integer)
    batting_eye = Column(Integer)
    c_lead = Column(Integer)
    batter_position = Column(String)  # Json形式で格納
    batter_box_count = Column(Integer)
    single_count = Column(Integer)
    double_count = Column(Integer)
    triple_count = Column(Integer)
    homerun_count = Column(Integer)
    batter_fourball_count = Column(Integer)
    batter_strikeout_count = Column(Integer)
    batter_runs = Column(Integer)
    contact_ex = Column(Integer)
    power_ex = Column(Integer)
    run_ex = Column(Integer)
    defence_ex = Column(Integer)
    throw_ex = Column(Integer)
    batting_eye_ex = Column(Integer)
    c_lead_ex = Column(Integer)
    speed = Column(Integer)
    stamina = Column(Integer)
    control = Column(Integer)
    henka = Column(Integer)
    out_count = Column(Integer)
    pitcher_runs = Column(Integer)
    pitcher_strikeout_count = Column(Integer)
    pitcher_fourball_count = Column(Integer)

    __tablename__ = 'player'

    # entityへの変換用メソッド
    def convert_to_entity(self):
        from baseball.entity.player import Player
        player = Player()
        player.set_name(self.name)
        player.set_school(self.school)
        player.grade = self.grade
        player.batter.set_contact(self.contact)
        player.batter.set_power(self.power)
        player.batter.set_run(self.run)
        player.batter.set_defence(self.defence)
        player.batter.set_throw(self.throw)
        player.batter.set_batting_eye(self.batting_eye)
        player.batter.set_c_lead(self.c_lead)
        player.batter.batter_position.position_pro = json.load(self.batter_position)
        player.batter.batter_stats.batter_box_count = self.batter_box_count
        player.batter.batter_stats.single_count = self.single_count
        player.batter.batter_stats.double_count = self.double_count
        player.batter.batter_stats.triple_count = self.triple_count
        player.batter.batter_stats.homerun_count = self.homerun_count
        player.batter.batter_stats.fourball_count = self.batter_fourball_count
        player.batter.batter_stats.strikeout_count = self.batter_strikeout_count
        player.batter.batter_stats.runs = self.batter_runs
        player.batter.batter_ex_point.contact = self.contact_ex
        player.batter.batter_ex_point.power = self.power_ex
        player.batter.batter_ex_point.run = self.run_ex
        player.batter.batter_ex_point.defence = self.defence_ex
        player.batter.batter_ex_point.throw = self.throw_ex
        player.batter.batter_ex_point.batting_eye = self.batting_eye_ex
        player.batter.batter_ex_point.c_lead = self.c_lead_ex
        player.pitcher.set_speed(self.speed)
        player.pitcher.set_stamina(self.stamina)
        player.pitcher.set_control(self.control)
        player.pitcher.set_henka(self.henka)
        player.pitcher.pitcher_stats.out_count = self.out_count
        player.pitcher.pitcher_stats.runs = self.pitcher_runs
        player.pitcher.pitcher_stats.strikeout_count = self.pitcher_strikeout_count
        player.pitcher.pitcher_stats.fourball_count = self.pitcher_fourball_count
        return player

    def create_table(self):
        Base.metadata.create_all(bind=Engine)


def get_players_by_team(team: str):
    return Session.query(PlayerData).filter_by(school=team)
