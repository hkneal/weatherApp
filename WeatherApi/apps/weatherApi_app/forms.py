from django import forms

class GetCityForm(forms.Form):
    city = forms.CharField(label='City', max_length=45, required=True)
