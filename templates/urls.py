"""
URL configuration for totalmarketing_entrega project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path
from totalmarketing_entrega.totalmarketing_entrega import views  # Importa el módulo de vistas de tu aplicación


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

