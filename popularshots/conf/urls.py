from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('',
    url(r'^shot/', include('shot.urls')),
    url(r'^admin/', include(admin.site.urls)),
)# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# urlpatterns += staticfiles_urlpatterns()

