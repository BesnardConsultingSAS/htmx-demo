from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from bier_shop.forms import BierCompanyForm, BierForm
from bier_shop.models import BierCompany, Bier


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


class AddBierView(View):
    def get(self, request, bier_company_id: int):
        return render(
            request,
            "bier_shop/components/bier_form.html",
            {"form": BierForm(), "bier_company_id": bier_company_id},
        )

    def post(self, request, bier_company_id: int):
        bier_form: BierForm = BierForm(request.POST, request.FILES)
        if bier_form.is_valid():
            bier_form.instance.bier_company_id = bier_company_id
            bier: Bier = bier_form.save()

            return render(
                request,
                template_name="bier_shop/components/bier_card.html",
                context={"bier": bier},
            )


class EditBierView(View):
    def get(self, request, bier_company_id: int, bier_id: int):
        bier: Bier = Bier.objects.get(id=bier_id)
        return render(
            request,
            "bier_shop/components/bier_form.html",
            {
                "form": BierForm(instance=bier),
                "bier": bier,
            },
        )

    def post(self, request, bier_company_id: int, bier_id: int):
        bier: Bier = Bier.objects.get(id=bier_id)
        bier_form: BierForm = BierForm(request.POST, request.FILES, instance=bier)
        if bier_form.is_valid():
            bier = bier_form.save()

            return render(
                request,
                template_name="bier_shop/components/bier_card.html",
                context={"bier": bier},
            )

        return render(
            request,
            "bier_shop/components/bier_form.html",
            {
                "form": bier_form,
                "bier": bier,
            },
        )


class DetailBierView(View):
    def get(self, request, bier_company_id: int, bier_id: int):
        bier: Bier = Bier.objects.get(id=bier_id)

        return render(
            request,
            template_name="bier_shop/components/bier_card.html",
            context={"bier": bier},
        )


class DeleteBierView(View):
    def get(self, request, bier_company_id: int, bier_id: int):
        Bier.objects.get(id=bier_id).delete()
        return HttpResponse("")
