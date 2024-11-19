from datetime import datetime

import factory
from factory.alchemy import SQLAlchemyModelFactory

from app.models import Animal, AnimalWeight, User


class BaseFactory(SQLAlchemyModelFactory):
    @classmethod
    def with_session(cls, session):
        cls._meta.sqlalchemy_session = session
        return cls


class UserFactory(BaseFactory):
    class Meta:
        model = User
        sqlalchemy_session = None

    email = factory.Faker('email')
    password = factory.Faker('password')
    first_name = 'First Name'


class AnimalFactory(factory.Factory):
    class Meta:
        model = Animal

    tag = 1
    gender = 'M'
    origin = 'Fazenda de Teste'
    sisbov = 1234
    breed = 'nelore'


class AnimalWeightFactory(factory.Factory):
    class Meta:
        model = AnimalWeight

    weight_type = 'buy'
    weight = 150.0
    weight_date = datetime.now()
