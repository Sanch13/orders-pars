from django import forms


class PriceForm(forms.Form):
    min_price = forms.DecimalField(min_value=0,
                                   required=False,
                                   widget=forms.NumberInput({'placeholder': "От"}))
    max_price = forms.DecimalField(min_value=0,
                                   required=False,
                                   widget=forms.NumberInput({'placeholder': "До"}))

