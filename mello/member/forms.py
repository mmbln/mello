# member/forms.py
# -*- coding: utf-8 -*-

from django import forms

from .models import Member

class MemberForm(forms.Form):
    login_name = forms.CharField(max_length=32,required=True)
    email = forms.EmailField(max_length=64)
    full_name = forms.CharField(max_length=64)
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

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        # TODO check for right format
        return full_name

