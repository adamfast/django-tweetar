from django import forms

class StationRegistrationForm(forms.Form):
    code = forms.CharField(max_length=6)
