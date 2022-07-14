# from xml.etree.ElementTree import Comment
from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import EmailPostForm, Comment

class EmailPostFormDjango(ModelForm):
    class Meta:
        model = EmailPostForm
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')