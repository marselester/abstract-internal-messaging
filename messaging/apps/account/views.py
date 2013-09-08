# coding: utf-8
from django.views import generic
from django.contrib.auth.models import Group

from messaging.common.decorators import ValidUserMixin


class Dashboard(ValidUserMixin, generic.TemplateView):

    template_name = 'account/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context['groups'] = Group.objects.all()
        return context
