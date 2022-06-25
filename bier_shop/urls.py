from django.http import HttpResponse
from django.urls import path

from bier_shop.views import BierCompanyListView, AddBierCompanyView

urlpatterns = [
    path("", BierCompanyListView.as_view(), name="bier-company-list"),
    path("add-bier-company", AddBierCompanyView.as_view(), name="add-bier-company"),
    path("cancel-form", lambda request: HttpResponse(), name="cancel-form"),
]
