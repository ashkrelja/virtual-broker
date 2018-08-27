from django import forms
from django.contrib.auth import get_user_model

class LicenseForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)
    city = forms.CharField(max_length=255)
    state = forms.CharField(max_length=255)
    zip = forms.CharField(max_length=255)

    class Meta:
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super(LicenseForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['address'].label = 'Address'
        self.fields['city'].label = 'City'
        self.fields['state'].label = 'State'
        self.fields['zip'].label = 'Zip'

class IncomeForm(forms.Form):
    income = forms.CharField(max_length=255)

    class Meta:
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super(IncomeForm,self).__init__(*args,**kwargs)
        self.fields['income'].label = 'Monthly Income'
