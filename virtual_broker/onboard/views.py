# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from formtools.wizard.views import SessionWizardView
from onboard.forms import LicenseForm, IncomeForm

# Create your views here.

class OnboardWizard(SessionWizardView):

    form_list = [LicenseForm, IncomeForm]
    template_name = 'onboard/onboard.html' #uses same html for each form

    def done(self, form_list, **kwargs):
        return render(self.request, 'done.html', {
            'form_data' : [form.cleaned_data for form in form_list]
            })
