from database import engine, Base, Session, AdvertisementModel, OwnerModel
from pytest import fixture
import time

@fixture(scope='session', autouse=True)
def prepare_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


@fixture()
def create_owner():
    with Session() as session:
        new_owner = OwnerModel(email=f'owner{time.time()}@email.ru', password='1111')
        session.add(new_owner)
        session.commit()
        return {
            'id': new_owner.id,
            'email': new_owner.email
        }


@fixture()
def create_advertisement():
    with Session() as session:
        new_owner = OwnerModel(email=f'owner{time.time()}@email.ru', password='1234')
        session.add(new_owner)
        session.commit()
        new_advertisement = AdvertisementModel(title='test', description='test_descr', owner_id=new_owner.id)
        session.add(new_advertisement)
        session.commit()
        return {
            'id': new_advertisement.id,
            'title': new_advertisement.title,
            'description': new_advertisement.description,
            'owner_id': new_advertisement.owner_id,
            'owner_email': new_owner.email
        }
