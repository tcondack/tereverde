from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls'))
]
if settings.DEBUG:
    # Fornece arquivos estáticos (CSS/JS)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
    
    # Fornece arquivos de MÍDIA (uploads de imagens)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)