from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.http import HttpResponse
import .views


urlpatterns = [
    url(r'^robots.txt', lambda x: HttpResponse("User-Agent: *\nDisallow: /", content_type="text/plain"), name="robots_file"),

    # using b/ as a prefix to all things which should never be publically visible
    url(r'^b/73aV/', admin.site.urls),
    url(r'^b/api-auth/', include('rest_framework.urls')),

    url(r'^accounts/', include('allauth.urls')),
    url(r'$', dhk.views.home),
]


if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    # using b/ as a prefix to all things which should never be publically visible
    urlpatterns = [url(r'^b/7v7/', include(debug_toolbar.urls))] + urlpatterns
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
