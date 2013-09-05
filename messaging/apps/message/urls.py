# coding: utf-8
from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'(?P<message_pk>[0-9]+)/$', views.MessageShow.as_view(),
        name='msg_show'),

    url(r'inbox/$', views.MessageInbox.as_view(), name='msg_inbox_list'),
    url(r'inbox/mark_as_read/$', views.MessageMarkAsRead.as_view(),
        name='msg_mark_as_read'),
    url(r'inbox/delete/$', views.MessageDelete.as_view(), name='msg_delete'),

    url(r'sent/$', views.MessageSent.as_view(), name='msg_sent_list'),

    url(r'compose/direct/$', views.MessageComposeDirect.as_view(),
        name='msg_compose_direct'),
    url(r'compose/broadcast/$', views.MessageComposeBroadcast.as_view(),
        name='msg_compose_broadcast'),
    url(r'compose/group/(?P<group_pk>[0-9]+)/$',
        views.MessageComposeGroup.as_view(), name='msg_compose_group'),
)
