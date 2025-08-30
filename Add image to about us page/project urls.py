from django.conf import settings
from django.conf.urls.static import static
from djnago.urls import path, include

urlpatterns = [
    path('', include('your_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_rrot=settings.MEDIA_ROOT)