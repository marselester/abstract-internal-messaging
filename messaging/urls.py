from django.conf.urls import patterns, include, url
from django.contrib import admin

from messaging.apps.account.views import Dashboard

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Dashboard.as_view(), name='dashboard'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^messages/', include('messaging.apps.message.urls')),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
