from bier_shop.models import BierCompany, Bier
from bier_shop.tests.factories.bier_company_factory import BierCompanyFactory
import pytest

from bier_shop.tests.factories.bier_factory import BierFactory


@pytest.mark.django_db
class TestModels:
    def test_bier_company_model_factory(self):
        BierCompanyFactory()

        assert BierCompany.objects.count() == 1

    def test_bier_model_factory(self):
        BierFactory()

        assert Bier.objects.count() == 1
