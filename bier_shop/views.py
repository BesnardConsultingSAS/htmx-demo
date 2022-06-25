from django.views.generic import ListView

from bier_shop.models import BierCompany


class BierCompanyListView(ListView):
    model = BierCompany
    template_name = "bier_shop/bier_company_list.html"
