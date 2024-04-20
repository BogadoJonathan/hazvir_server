
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/hazvir/',include('hazvir.urls')),
    path('api/v1/granConexion/',include('granConexion.urls'))
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
