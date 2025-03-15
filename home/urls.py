from django.urls import path
from . import views
from django.conf.urls.static import static
from core import settings
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path("admin/", admin.site.urls),      # Admin por último
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
