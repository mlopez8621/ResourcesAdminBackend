from django.conf.urls import url

from resourcesApp.Views import RecursoViews

urlpatterns = [
    url(r'^recurso$', RecursoViews.recursos_list)
]