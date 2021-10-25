from django import forms
from django.contrib.auth import get_user_model
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import fields
from django.forms.widgets import ChoiceWidget, Select
from .models import User, Post

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


    following = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name='Following',
            is_stacked=False
        )
    )

class PostChangeForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
    author = forms.ModelChoiceField(queryset=User.objects.all())

