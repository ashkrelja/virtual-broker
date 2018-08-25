from django.conf.urls import url

from . import forms
from . import views

app_name = 'onboard'

urlpatterns = [
    url(r'^new/$', views.OnboardWizard.as_view([forms.LicenseForm, forms.IncomeForm]), name='create')
]
