from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib import messages

from .forms import UserRegisterForm

class Register(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        form.save()
        messages.success(self.request, f'Account created for {username}!')

        return super().form_valid(form)

