"""fundacion URL Configuration
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include

from django.conf.urls import handler404, handler500

from applications.home.views import Error404View, Error500View

urlpatterns = (
    [
        path('admin/', admin.site.urls),

        re_path('', include('applications.home.urls')),
        re_path('', include('applications.users.urls')),
        re_path('', include('applications.entrada.urls')),
        re_path('', include('applications.favoritos.urls')),
        re_path('', include('applications.esal.urls')),

        # urls para ckeditor para
        re_path(r'^ckeditor/', include("ckeditor_uploader.urls")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)

handler404 = Error404View.as_view()
handler500 = Error500View.as_error_view()
