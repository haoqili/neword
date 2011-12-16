from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'apps.basic.views.index'),
    url(r'^basic/$', 'apps.basic.views.index'),
    url(r'^admin/', include(admin.site.urls)),
)
