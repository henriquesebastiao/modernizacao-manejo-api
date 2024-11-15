from enum import Enum


class Breeds(str, Enum):
    ANGUS = 'angus'
    BRAHMAN = 'brahman'
    GIR_LEITEIRO = 'gir_leiteiro'
    GIROLANDO = 'girolando'
    GUZERA = 'guzera'
    HOLANDES = 'holandes'
    NELORE = 'nelore'
    SINDI = 'sindi'
    SENEPOL = 'senepol'
    TABAPUA = 'tabapua'


class EmploymentPositions(str, Enum):
    COWBOY = 'cowboy'
    FARMER = 'farmer'
    MANAGER = 'manager'


class FarmerPlan(str, Enum):
    FREE = 'free'
    PRO = 'pro'
    STARTER = 'starter'


class Genders(str, Enum):
    F = 'f'
    M = 'm'


class WeightTypes(str, Enum):
    BIRTH = 'birth'
    BUY = 'buy'
    SELL = 'sell'
    WEANING = 'weaning'
