# coding: utf-8
from django.views import generic

from messaging.common.decorators import ValidUserMixin


class Dashboard(ValidUserMixin, generic.TemplateView):

    template_name = 'account/dashboard.html'
