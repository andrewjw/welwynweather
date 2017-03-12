from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import app.views

urlpatterns = [
    url(r'^$', app.views.index),
    url(r'^(\d\d\d\d)/(\d\d?)/(\d\d?)$', app.views.day, name='day'),
    url(r'^(\d\d\d\d)/(\d\d?)$', app.views.month, name='month'),
    url(r'^(\d\d\d\d)$', app.views.year, name='year'),
    url(r'^about$', app.views.about),
    url(r'^records$', app.views.records),

    # Examples:
    # url(r'^$', 'weather.views.home', name='home'),
    # url(r'^weather/', include('weather.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]

try:
    import electricity.views
except ImportError:
    pass
else:
    urlpatterns += [
       url(r'^electricity/?$', electricity.views.index),
       url(r'^electricity/(\d\d\d\d)/(\d\d?)/(\d\d?)$', electricity.views.day),
    ]
