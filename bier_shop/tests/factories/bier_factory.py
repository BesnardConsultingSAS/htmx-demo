import factory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice, FuzzyText
from bier_shop.models import Bier
from bier_shop.tests.factories.bier_company_factory import BierCompanyFactory


class BierFactory(DjangoModelFactory):
    class Meta:
        model = Bier

    name = factory.Faker("company")
    image = factory.django.ImageField()
    bier_company = factory.SubFactory(BierCompanyFactory)
    bier_type = FuzzyChoice(choices=Bier.BierType.choices)
    description = FuzzyText()
