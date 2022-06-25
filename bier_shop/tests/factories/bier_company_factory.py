import factory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice, FuzzyText
from django_countries.data import COUNTRIES

from bier_shop.models import BierCompany


class BierCompanyFactory(DjangoModelFactory):
    class Meta:
        model = BierCompany

    name = factory.Faker("company")
    logo = factory.django.ImageField()
    country = FuzzyChoice(COUNTRIES.values())
    description = FuzzyText()
