from django import forms
from django.contrib.auth import get_user_model
from models import Onboard

class LicenseForm(forms.ModelForm):

    class Meta:
        model = Onboard
        fields = [
            'first_name',
            'last_name',
            'address',
            'city',
            'state',
            'zip'
        ]

    def __init__(self,*args,**kwargs):
        super(LicenseForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['address'].label = 'Address'
        self.fields['city'].label = 'City'
        self.fields['state'].label = 'State'
        self.fields['zip'].label = 'Zip'

class IncomeForm(forms.ModelForm):

    class Meta:
        model = Onboard
        fields = [
            'income'
        ]

    def __init__(self,*args,**kwargs):
        super(IncomeForm,self).__init__(*args,**kwargs)
        self.fields['income'].label = 'Monthly Income'
