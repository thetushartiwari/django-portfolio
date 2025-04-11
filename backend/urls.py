import os 
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'frontend', 'static'))
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
