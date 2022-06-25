from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from bier_shop.models import BierCompany


class BierCompanyListView(ListView):
    model = BierCompany
    template_name = "bier_shop/bier_company_list.html"


class AddBierCompanyView(View):
    def get(self, request):
        return render(request, "bier_shop/components/add_bier_company_form.html")
