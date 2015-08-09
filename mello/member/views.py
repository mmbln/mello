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
    members = Member.objects.all()
    return render(request, 'member_list.html', {'members': members})

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            # All data entered correctly, save the data
            temp_password = generate_password()
            login_name = form.cleaned_data['login_name']
            email = form.cleaned_data['email']
            full_name = form.cleaned_data['full_name']
            if form.cleaned_data['admin']:
                Member.objects.create_superuser(email=email,
                                                login_name=login_name,
                                                password=temp_password,
                                                full_name=full_name)
            else:
                Member.objects.create_user(email=email,
                                           login_name=login_name,
                                           password=temp_password,
                                           full_name=full_name)
            # TODO send email to user
            return HttpResponseRedirect(reverse('member_list'))
        else:
            # Show form with errors
            print('Form is not valid')
    else:
        form = MemberForm()
    
    return render(request, 'member_new.html', {'form': form})

def edit_member(request):
    form = MemberForm()
    return render(request, 'member_new.html')
