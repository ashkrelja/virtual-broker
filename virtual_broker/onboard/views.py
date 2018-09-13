# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from formtools.wizard.views import SessionWizardView
from onboard.forms import LicenseForm, IncomeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from braces.views import SelectRelatedMixin
from models import Onboard

# Create your views here.

class OnboardWizard(LoginRequiredMixin, SelectRelatedMixin, SessionWizardView):

    form_list = [LicenseForm, IncomeForm]
    template_name = 'onboard/onboard.html' #uses same html for each form

    def done(self, form_list, **kwargs):

        instance = Onboard()
        for form in form_list:
            for field, value in form.cleaned_data.iteritems():
                setattr(instance, field, value)
        instance.user = self.request.user
        instance.save()
        return render(self.request, 'onboard/done.html', {
            'form_data' : [form.cleaned_data for form in form_list]
            })
