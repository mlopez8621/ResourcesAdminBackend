from django.conf.urls import url

from resourcesApp.Views import RecursoViews, RecursoResponsableViews, ComentarioViews


urlpatterns = [
    url(r'^recurso$', RecursoViews.recursos_list),
    url(r'^recurso_res/(\d+)/$', RecursoResponsableViews.recursoResponsable_list),
    url(r'^lista-chequeo/(\d+)/$', RecursoViews.recursoListaChequeo_list)
]