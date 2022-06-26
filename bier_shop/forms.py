from crispy_forms.helper import FormHelper
from django import forms

from bier_shop.models import BierCompany, Bier


class BierCompanyForm(forms.ModelForm):
    class Meta:
        model = BierCompany
        fields = ["name", "logo", "country", "description"]

        widgets = {
            "description": forms.Textarea(
                attrs={"rows": "3"},
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control-sm"


class BierForm(forms.ModelForm):
    class Meta:
        model = Bier
        fields = ["name", "image", "bier_type", "description"]

        widgets = {
            "description": forms.Textarea(
                attrs={"rows": "3"},
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control-sm"
        self.helper = FormHelper(self)
        self.helper.form_tag = False
