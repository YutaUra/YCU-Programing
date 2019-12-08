from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin, admindocs
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('markdownx/', include('markdownx.urls')),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    path('', include('django_press.urls')),
]
