# coding=utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^conta/$', views.index, name='index'),
    url(r'^alterar-dados/$', views.alterar_dados_usuario, name='alterar-dados-usuario'),
    url(r'^alterar-senha/$', views.update_password, name='update_password'),
    url(r'^registro/$', views.register, name='register'),
]

