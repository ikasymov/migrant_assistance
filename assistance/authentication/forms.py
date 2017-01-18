#coding= utf-8
from __future__ import unicode_literals
from django import forms
from django.utils.translation import ugettext_lazy as _
from authentication.models import User


class SignInForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': _('Ведите Эл.почту'), 'type': 'email', 'class': 'form-control mb-2 mr-sm-2 mb-sm-0'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': _('Ведите пароль'), 'class': 'form-control mb-2 mr-sm-2 mb-sm-0'}))


class SignupForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': _('Ведите Эл.почту'), 'type': 'email', 'class': 'form-control mb-2 mr-sm-2 mb-sm-0'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': _('Ведите пароль'), 'class': 'form-control mb-2 mr-sm-2 mb-sm-0'}))
    check_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': _('Ведите пароль еше раз'), 'class': 'form-control mb-2 mr-sm-2 mb-sm-0'}))
