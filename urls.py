from django.urls import path
from . import views  # Importa el módulo de vistas de tu aplicación


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('paquetes/', views.lista_paquetes, name='lista_paquetes'),
    path('paquete/<int:pk>/', views.detalle_paquete, name='detalle_paquete'),
    path('paquete/comentar/<int:pk>/', views.comentar_paquete, name='comentar_paquete'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
]

# urls.py del proyecto

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),  # Incluye las URLs de autenticación
    path('', include('totalmarketing_entrega.urls')),  
    
]
