# member/forms.py
# -*- coding: utf-8 -*-

from django import forms

from .models import Member

class MemberForm(forms.Form):
    login_name = forms.CharField(max_length=100,required=True)
    email = forms.EmailField(max_length=1000)
    admin = forms.BooleanField()

    def clean_login_name(self):
        ln = self.cleaned_data.get('login_name')
        try:
            Member.objects.get(login_name=ln)
        except:
            return ln
        raise forms.ValidationError('Login Name already exists')


    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            Member.objects.get(email=email)
        except:
            return email
        raise forms.ValidationError('Email Address already exists')


