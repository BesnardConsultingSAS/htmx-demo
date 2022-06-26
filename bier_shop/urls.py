from django.http import HttpResponse
from django.urls import path

from bier_shop.views import (
    BierCompanyListView,
    AddBierCompanyView,
    DeleteBierCompanyView,
    BierCompanyDetailsView,
    AddBierView,
    EditBierView,
    DetailBierView,
)

urlpatterns = [
    path("", BierCompanyListView.as_view(), name="bier-company-list"),
    path(
        "bier-company/<int:pk>/",
        BierCompanyDetailsView.as_view(),
        name="bier-company-details",
    ),
    path("add-bier-company/", AddBierCompanyView.as_view(), name="add-bier-company"),
    path(
        "bier-company/<int:bier_company_id>/add-bier/",
        AddBierView.as_view(),
        name="add-bier",
    ),
    path(
        "bier-company/<int:bier_company_id>/edit-bier/<int:bier_id>/",
        EditBierView.as_view(),
        name="edit-bier",
    ),
    path(
        "bier-company/<int:bier_company_id>/detail-bier/<int:bier_id>/",
        DetailBierView.as_view(),
        name="detail-bier",
    ),
    path(
        "delete-bier-company/<int:pk>/",
        DeleteBierCompanyView.as_view(),
        name="delete-bier-company",
    ),
    path("cancel-form/", lambda request: HttpResponse(), name="cancel-form"),
]
