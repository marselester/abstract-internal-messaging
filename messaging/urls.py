from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^messages/', include('messaging.apps.message.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
