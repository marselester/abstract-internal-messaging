# coding: utf-8
from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^$', views.MessageList.as_view(), name='msg_list'),
    url(r'(?P<message_pk>[0-9]+)/$', views.MessageShow.as_view(),
        name='msg_show'),

    url(r'compose/$', views.MessageComposeParticular.as_view(),
        name='msg_compose_particular'),
    url(r'compose/broadcast/$', views.MessageComposeBroadcast.as_view(),
        name='msg_compose_broadcast'),
    url(r'compose/group/$', views.MessageComposeGroup.as_view(),
        name='msg_compose_group'),

    url(r'mark_as_read/$', views.MessageMarkAsRead.as_view(),
        name='msg_mark_as_read'),
    url(r'delete/$', views.MessageDelete.as_view(), name='msg_delete'),
)
