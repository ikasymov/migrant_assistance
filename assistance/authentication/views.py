# coding= utf-8
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.views.generic import FormView
from django.contrib.auth import authenticate, login
from django.contrib import messages

from authentication.forms import SignInForm, SignupForm
from authentication.models import User
from main.messages import Messages


class SignInView(FormView):
    template_name = 'authentication/sign_in.html'
    form_class = SignInForm
    message_error = Messages.Authenticated.signin_message_error
    message_success = Messages.Authenticated.signin_message_success

    def get_success_url(self):
        self.success_url = self.request.META['HTTP_REFERER']
        return self.success_url

    def form_valid(self, form):
        user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
        if user is not None:
            login(self.request, user)
            messages.add_message(self.request, messages.SUCCESS, self.message_success)
        else:
            messages.add_message(self.request, messages.WARNING, self.message_error)
        return super(SignInView, self).form_valid(form)


class SignUpView(FormView):
    form_class = SignupForm
    template_name = 'authentication/sign_up.html'
    message_success = Messages.Authenticated.signup_message_success
    message_error = Messages.Authenticated.signup_message_error
    message_exist = Messages.Authenticated.signup_message_success_exist

    def get_success_url(self):
        self.success_url = self.request.META['HTTP_REFERER']
        return self.success_url

    def form_valid(self, form):
        email_value = form.cleaned_data['email']
        try:
            User.objects.get(email=email_value)
            messages.add_message(self.request, messages.WARNING, self.message_exist)
            return redirect(self.request.path)
        except User.DoesNotExist:
            if form.cleaned_data['check_password'] == form.cleaned_data['password']:
                user = User.objects.create(email=email_value)
                user.set_password(form.cleaned_data['password'])
                user.save()
                messages.add_message(self.request, messages.SUCCESS, self.message_success)
            else:
                messages.warning(self.request, self.message_error)
            return super(SignUpView, self).form_valid(form)
