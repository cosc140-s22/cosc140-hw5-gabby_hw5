from django import forms

class ProductFilterForm(forms.Form):
    name_search = forms.CharField(label="Name search", max_length=50, required=False)
    min_price = forms.DecimalField(label="Minimum price", decimal_places = 2, required=False)
    max_price = forms.DecimalField(label="Maximum price", decimal_places = 2, required=False)
