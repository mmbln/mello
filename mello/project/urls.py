# project/urls.py
# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.view_project_list, name='project_list'),
    url(r'^new/', views.add_project, name='add_project'),
#    url(r'^(?P<id>\d+)/$', project.views.view_project, name='project_view'),
#    url(r'^new/$', project.views.new_project, name='project_new'),
]
