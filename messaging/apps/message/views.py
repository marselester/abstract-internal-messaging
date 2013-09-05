# coding: utf-8
from django.views import generic


class MessageList(generic.ListView):

    pass


class MessageShow(generic.DetailView):

    pass


class MessageComposeParticular(generic.View):

    pass


class MessageComposeBroadcast(generic.View):

    pass


class MessageComposeGroup(generic.View):

    pass


class MessageMarkAsRead(generic.View):

    pass


class MessageDelete(generic.View):

    pass
