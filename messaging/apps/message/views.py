# coding: utf-8
from django.views import generic
from django.contrib import messages as flash_messages
from django.shortcuts import redirect

from messaging.common.decorators import ValidUserMixin
from messaging.apps.message import tasks
from . import forms


class MessageInbox(ValidUserMixin, generic.ListView):

    pass


class MessageSent(ValidUserMixin, generic.ListView):

    pass


class MessageShow(ValidUserMixin, generic.DetailView):

    pass


class MessageComposeDirect(ValidUserMixin, generic.View):

    pass


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


class MessageComposeGroup(ValidUserMixin, generic.View):

    pass


class MessageMarkAsRead(ValidUserMixin, generic.View):

    pass


class MessageDelete(ValidUserMixin, generic.View):

    pass
