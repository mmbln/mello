# member/views
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import MemberForm

def view_member_list(request):
    return render(request, 'member_list.html')

def add_member(request):
    form = MemberForm()
    print(form.as_p())
    return render(request, 'member_new.html')

def edit_member(request):
    form = MemberForm()
    return render(request, 'member_new.html')
