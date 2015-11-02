# member/urls.py
# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'member.views.view_member_list', name='member_list'),
    url(r'^new/', 'member.views.add_member', name='add_member'),
    url(r'^img/(?P<id>\d+)', 'member.views.show_img', name='member_img_small'),
#    url(r'^(?P<id>\d+)/$', 'project.views.view_project', name='project_view'),
#    url(r'^new/$', 'project.views.new_project', name='project_new'),
]
