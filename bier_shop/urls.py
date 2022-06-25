from django.urls import path

from bier_shop.views import BierCompanyListView

urlpatterns = [
    path("", BierCompanyListView.as_view(), name="bier-company-list"),
]
