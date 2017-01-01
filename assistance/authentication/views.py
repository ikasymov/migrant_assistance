# coding= utf-8
from django.views.generic import FormView
from django.contrib.auth import authenticate, login
from django.contrib import messages

from authentication.forms import SignInForm, SignupForm
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
            messages.add_message(self.request, messages.ERROR, self.message_error)
        return super(SignInView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SignInView, self).get_context_data(**kwargs)
        context['forms'] = SignInForm()
        return context


class SignUpView(FormView):
    form_class = SignupForm
    template_name = 'authentication/sign_up.html'
    message_success = Messages.Authenticated.signup_message_succes

    def get_success_url(self):
        self.success_url = self.request.META['HTTP_REFERER']
        return self.success_url

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.set_password(form.cleaned_data['password'])
        obj.save()
        messages.add_message(self.request, messages.SUCCESS, self.message_success)
        return super(SignUpView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        context['forms'] = SignupForm()
        return context
