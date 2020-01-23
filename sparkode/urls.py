"""sparkode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pnl.views import principal, login,acercade,temario, registro, logOut, TestAprendizaje, tema, EjercicioEj, Ejercicios, evaluar, evaluarK, ultimaConexion, perfil, recuperarContra, fotoPerfil
urlpatterns = [
    path('admin/', admin.site.urls),
    path('principal/', principal),
    path('login/', login),
    path('temario/', temario),
    path('', login),
    path('acercade/', acercade),
    path('registro/', registro),
    path('logOut/', logOut),
    path('TestAprendizaje/', TestAprendizaje),
    path('tema/<int:tema>/<int:subtema>/<int:pagina>', tema),
    path('ejercicioEj/<str:clave>/<int:subtema>/<str:tipo>/<int:numero>', EjercicioEj),
    path('ejercicio/<str:clave>',Ejercicios),
    path('evaluar/<str:clave>/<int:subtema>/<str:tipo>/<int:numero>', evaluar),
    path('evaluarK/<str:clave>/<int:subtema>/<str:tipo>/<int:numero>', evaluarK),
    path('ultimaConexion', ultimaConexion),
    path('perfil/', perfil),
    path('recuperar/', recuperarContra),
    path('fotoPerfil/',fotoPerfil)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)