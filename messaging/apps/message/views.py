# coding: utf-8
from django.views import generic

from messaging.common.decorators import ValidUserMixin


class MessageInbox(ValidUserMixin, generic.ListView):

    pass


class MessageSent(ValidUserMixin, generic.ListView):

    pass


class MessageShow(ValidUserMixin, generic.DetailView):

    pass


class MessageComposeDirect(ValidUserMixin, generic.View):

    pass


class MessageComposeBroadcast(ValidUserMixin, generic.View):

    pass


class MessageComposeGroup(ValidUserMixin, generic.View):

    pass


class MessageMarkAsRead(ValidUserMixin, generic.View):

    pass


class MessageDelete(ValidUserMixin, generic.View):

    pass
