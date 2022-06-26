from django.http import HttpResponse
from django.urls import path

from bier_shop.views import (
    BierCompanyListView,
    AddBierCompanyView,
    DeleteBierCompanyView,
)

urlpatterns = [
    path("", BierCompanyListView.as_view(), name="bier-company-list"),
    path("add-bier-company/", AddBierCompanyView.as_view(), name="add-bier-company"),
    path(
        "delete-bier-company/<int:pk>/",
        DeleteBierCompanyView.as_view(),
        name="delete-bier-company",
    ),
    path("cancel-form/", lambda request: HttpResponse(), name="cancel-form"),
]
