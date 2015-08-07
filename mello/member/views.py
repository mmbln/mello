# member/views
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import MemberForm
from .models import Member

#----------------------------------------------------------------
# utils
#----------------------------------------------------------------

def generate_password():
    # TODO use random generator
    return ('123')

#----------------------------------------------------------------
# views
#----------------------------------------------------------------

def view_member_list(request):
    return render(request, 'member_list.html')

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            print('Form is valid')
            # All data entered correctly, save the data
            temp_password = generate_password()
            login_name = form.cleaned_data['login_name']
            email = form.cleaned_data['email']
            if form.cleaned_data['admin']:
                Member.objects.create_superuser(email=email,
                                                login_name=login_name,
                                                password=temp_password)
            else:
                Member.objects.create_user(email=email,
                            login_name=login_name,
                            password=temp_password)
            # TODO send email to user
            HttpResponseRedirect(reverse('member_list'))
        else:
            # Show form with errors
            print('Form is not valid')
    else:
        form = MemberForm()
    
    return render(request, 'member_new.html')

def edit_member(request):
    form = MemberForm()
    return render(request, 'member_new.html')
