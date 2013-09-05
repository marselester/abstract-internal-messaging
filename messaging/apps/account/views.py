# coding: utf-8
from django.views import generic


class Dashboard(generic.TemplateView):

    template_name = 'account/dashboard.html'
