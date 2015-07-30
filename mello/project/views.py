# proect/views
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import ProjectForm

def home(request):
    return HttpResponseRedirect(reverse('project_list'))

def view_project_list(request):
    return render(request, 'project_list.html')

def add_project(request):
    form = ProjectForm()
    return render(request, 'project_new.html')

def edit_project(request):
    return render(request, 'project_new.html')
     

