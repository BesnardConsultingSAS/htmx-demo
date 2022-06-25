from django.test.client import Client
import pytest

from bier_shop.tests.factories.bier_company_factory import BierCompanyFactory


@pytest.mark.django_db
class TestBierCompanyListView:
    def test_bier_company_list_view_url_is_working(self, client: Client):
        bier_company = BierCompanyFactory()

        response = client.get("")

        template_used: list[str] = [template.name for template in response.templates]

        assert response.status_code == 200
        assert list(response.context_data["biercompany_list"]) == [bier_company]
        assert "bier_shop/bier_company_list.html" in template_used
