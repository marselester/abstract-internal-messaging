# coding: utf-8
from django.views import generic
from django.contrib import messages as flash_messages
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import Group

from messaging.common.decorators import ValidUserMixin
from messaging.apps.message import tasks
from . import forms


class MessageInbox(ValidUserMixin, generic.ListView):

    pass


class MessageSent(ValidUserMixin, generic.ListView):

    pass


class MessageShow(ValidUserMixin, generic.DetailView):

    pass


class MessageComposeDirect(ValidUserMixin, generic.CreateView):

    form_class = forms.MessageComposeDirectForm
    template_name = 'message/compose_direct.html'

    def form_valid(self, form):
        user = self.request.user

        message = form.save(False)
        message.sender = user
        message.save()

        recipients_pks = form.cleaned_data['recipients']
        tasks.send_direct_message.delay(message.pk, recipients_pks)

        flash_messages.success(self.request, 'Direct message was sent.')

        return redirect('dashboard')


class MessageComposeBroadcast(ValidUserMixin, generic.CreateView):

    form_class = forms.MessageComposeBroadcastForm
    template_name = 'message/compose_broadcast.html'

    def form_valid(self, form):
        user = self.request.user

        message = form.save(False)
        message.sender = user
        message.save()

        tasks.send_broadcast_message.delay(message.pk)

        flash_messages.success(self.request, 'Broadcast message was sent.')

        return redirect('dashboard')


class MessageComposeGroup(ValidUserMixin, generic.CreateView):

    form_class = forms.MessageComposeGroupForm
    template_name = 'message/compose_group.html'

    def dispatch(self, request, *args, **kwargs):
        self.group = get_object_or_404(Group, pk=kwargs['group_pk'])
        return super(MessageComposeGroup, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MessageComposeGroup, self).get_context_data(**kwargs)
        context['group'] = self.group
        return context

    def form_valid(self, form):
        user = self.request.user

        message = form.save(False)
        message.sender = user
        message.save()

        tasks.send_group_message.delay(message.pk, self.group.pk)

        flash_messages.success(self.request, 'Group message was sent.')

        return redirect('dashboard')


class MessageMarkAsRead(ValidUserMixin, generic.View):

    pass


class MessageDelete(ValidUserMixin, generic.View):

    pass
