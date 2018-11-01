# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from resourcesApp.models import Estado, Rol, Responsable, Recurso, Recurso_Responsable, \
    Recurso_Intermedio, Lista_Chequeo, Resultado_ListaChequeo, Recurso_Comentario,Tipo_Recurso

admin.site.register(Tipo_Recurso);
admin.site.register(Estado);
admin.site.register(Rol);
admin.site.register(Responsable);
admin.site.register(Recurso);
admin.site.register(Recurso_Responsable);
admin.site.register(Recurso_Intermedio);
admin.site.register(Recurso_Comentario);
admin.site.register(Lista_Chequeo);
admin.site.register(Resultado_ListaChequeo);
