# member/forms.py
# -*- coding: utf-8 -*-

from django import forms

class MemberForm(forms.Form):
    login_name = forms.CharField(max_length=100,required=True)
    email = forms.EmailField(max_length=1000)
    admin = forms.BooleanField()
    
