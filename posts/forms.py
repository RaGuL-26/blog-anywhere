from django import forms
from . import models

class InputForms(forms.ModelForm):
    class Meta:
        model = models.postBlog
        fields = ['title','images','about_post','slug']
    