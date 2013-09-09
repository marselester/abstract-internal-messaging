# coding: utf-8
from django.views import generic
from django.contrib.auth.models import Group

from messaging.common.decorators import ValidUserMixin
from messaging.apps.message.models import Message


class Dashboard(ValidUserMixin, generic.TemplateView):

    template_name = 'account/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context['groups'] = Group.objects.all()

        user = self.request.user
        # TODO: It should be cached.
        context['inbox'] = Message.objects.unread_by_user_id(user.pk) \
            .select_related('sender')
        context['inbox_count'] = Message.objects.unread_count_by_user_id(user.pk)
        # TODO: It should be cached.
        context['inbox_total_count'] = user.inbox.count()
        return context
