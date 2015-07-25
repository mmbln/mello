# proect/views
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.


def home(request):
    return HttpResponseRedirect(reverse('project_list'))

def view_project_list(request):
    return HttpResponse('Hallo')

