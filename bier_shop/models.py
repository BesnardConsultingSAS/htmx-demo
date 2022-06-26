from django.db import models
from django_countries.fields import CountryField


class BierCompany(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to="bier_company")
    country = CountryField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Bier(models.Model):
    class BierType(models.TextChoices):
        PILSNER = "Pilsner"
        DARK_LAGER = "Dark Lager"
        GERMAN_BOCK = "German Bock"
        BROWN_ALE = "Brown Ale"
        PALE_ALE = "Pale Ale"
        INDIAN_PALE_ALE = "India Pale Ale"
        PORTER = "Porter"
        STOUT = "Stout"

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="bier")
    bier_company = models.ForeignKey(BierCompany, on_delete=models.CASCADE)
    bier_type = models.CharField(choices=BierType.choices, max_length=100)
    description = models.TextField()
