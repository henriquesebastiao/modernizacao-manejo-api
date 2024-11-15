from datetime import datetime

import factory

from app.models import Animal, AnimalWeight, User


class UserFactory(factory.Factory):
    class Meta:
        model = User

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
