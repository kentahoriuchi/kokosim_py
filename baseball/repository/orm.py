from baseball.repository.mapper_setting import Session


def insert(model):
    Session.add(instance=model)
    Session.commit()


def insert_all(model: list):
    Session.add_all(instances=model)
    Session.commit()


def update(model, input_model, target_id: int):
    target = Session.query(model).filter_by(id=target_id).one()
    target = input_model
    Session.commit()


def delete(model, target_id: int):
    target = Session.query(model).filter_by(id=target_id).one()
    Session.delete(target)
    Session.commit()


def delete_all(model):
    Session.query(model).delete()
    Session.commit()


def read(model, target_id: int):
    result = Session.query(model).filter_by(id=target_id).one()
    return result
