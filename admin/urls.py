"""admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers

from resourcesApp.Views.EstadoViews import EstadosViewSet
from resourcesApp.Views.RecursoViews import RecursoViewSet
from resourcesApp.Views.ResponsableViews import ResponsableViewSet
from resourcesApp.Views.RecursoResponsableViews import RecursoResponsableViewSet

router = routers.DefaultRouter()
router.register(r'estados', EstadosViewSet)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^recursos-filtrados/?', RecursoViewSet.as_view()),
    url('^responsable/', ResponsableViewSet.as_view()),
    url('^recurso-responsable/', RecursoResponsableViewSet.as_view()),
    url(r'^', include(router.urls))
]
