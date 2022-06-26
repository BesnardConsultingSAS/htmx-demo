from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from bier_shop.forms import BierCompanyForm, BierForm
from bier_shop.models import BierCompany


class BierCompanyListView(ListView):
    model = BierCompany
    template_name = "bier_shop/bier_company_list.html"


class AddBierCompanyView(View):
    def get(self, request):
        return render(
            request,
            "bier_shop/components/add_bier_company_form.html",
            {"form": BierCompanyForm()},
        )

    def post(self, request):
        form = BierCompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(
                request,
                "bier_shop/components/bier_company_card.html",
                {"bier_company": form.instance},
            )
        return render(
            request,
            "bier_shop/components/add_bier_company_form.html",
            {"form": form},
        )


class DeleteBierCompanyView(View):
    def get(self, request, pk: int):
        BierCompany.objects.get(id=pk).delete()
        return HttpResponse("")


class BierCompanyDetailsView(View):
    def get(self, request, pk: int):
        bier_company = BierCompany.objects.get(id=pk)
        return render(
            request,
            "bier_shop/bier_company_details.html",
            {"bier_company": bier_company, "biers": bier_company.bier_set.all()},
        )

    def post(self, request, pk: int):
        bier_company = BierCompany.objects.get(id=pk)
        context = {"bier_company": bier_company, "biers": bier_company.bier_set.all()}
        if request.POST.get("add-empty-bier-form"):
            context["form_new_bier"] = BierForm()
        return render(
            request,
            "bier_shop/bier_company_details.html",
            context,
        )
