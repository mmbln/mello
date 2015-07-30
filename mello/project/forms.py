# proect/forms.py
# -*- coding: utf-8 -*-

from django import forms

class ProjectForm(forms.Form):
    project_name = forms.CharField(max_length=100,required=True)
    description = forms.CharField(max_length=1000)

    
