from django.conf.urls import url

from onboard.forms import LicenseForm, IncomeForm
from onboard.views import OnboardWizard

urlpatters = [
    url(r'^contact/$', ContactWizard.as_view([LicenseForm, IncomeForm]), name='onboarding'),
]
