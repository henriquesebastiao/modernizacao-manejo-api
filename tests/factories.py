import factory

from app.models import Animal, Breed, User


class UserFactory(factory.Factory):
    class Meta:
        model = User

    email = factory.Faker('email')
    password = factory.Faker('password')


class AnimalFactory(factory.Factory):
    class Meta:
        model = Animal

    tag = 1
    gender = 'M'
    origin = 'Fazenda de Teste'
    sisbov = 1234


class BreedFactory(factory.Factory):
    class Meta:
        model = Breed

    name = 'Raca das Vaquinhas Intrusas'
