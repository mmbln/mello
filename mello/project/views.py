# proect/views
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def home(request):
    return HttpResponse('Hallo')

