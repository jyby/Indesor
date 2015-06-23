#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.utils.encoding import smart_str
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'indesor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^acerca_del_proyecto/$', 'api.views.about'),
    url(r'^como_funciona/$', 'api.views.how_it_works'),
    url(r'^subir_video/$', 'api.views.upload_video'),    
    url(r'^subir_video_palabra_nueva/$', 'api.views.upload_video_new_word'),
    url(r'^subir_video_palabra_existente/$', 'api.views.upload_video_existing_word'),    
    url(r'^subir_definicion/$', 'api.views.upload_definition'),
    url(r'^listado_archivos/$', 'api.views.files_to_validate'),    
    url(r'^validar_archivo/$', 'api.views.validate'),
    url(r'^desafio/$', 'api.views.challenge'),
    url(r'^desafio_video/$', 'api.views.video_challenge'),
    url(r'^resultado/$', 'api.views.video_challenge_result'),

    url(r'^registrar_usuarios/$','api.views.create_user'),
    url(r'^iniciar_sesion/$','api.views.login'),
    url(r'^cerrar_sesion/$','api.views.logout'),

    url(r'^modificar_contrasena/$','api.views.change_password'),

    url(r'^pagar_por_palabra/$','api.views.pay_per_word'), 

    url(r'^error/$','api.views.error'), 

    url(r'^orden_alfabetico/(?P<letra>[a-zA-ZñÑ]{1})/$', 'api.views.get_words'),
    url(r'^configuracion_manual/(?P<manual_configuration>[0-9]{2})/$', 'api.views.get_words_manual_config'),
)
