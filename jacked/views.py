from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView
from django.contrib.auth.models import User
from django.contrib import messages

from .models import MacroCycle
from .forms import MacroForm
# Create your views here.

class Home(TemplateView):
    template_name = 'jacked/front_page.html'

    def get(self, request):
        users = User.objects.all()
        return render(request, self.template_name, {'users': users})


def macro_cycle(request, *args, **kwargs):
    user_id = kwargs.get('user_id')
    form = MacroForm()
    macros = MacroCycle.objects.filter(user=user_id)
    if request.method == 'GET':
        return render(request, "jacked/macros.html", {'form': form})
    elif request.method == 'POST':
        form_input = MacroForm(request.POST)

        if  form_input.is_valid():
            f =  form_input.save(commit=False)
            f.user = request.user
            f.save()
            messages.success(request, 'Form valid')
        else:
            messages.error(request, 'Form invalid')
    return render(request, "jacked/macros.html", {'form': form, 'macros': macros})


class MacroCycles(TemplateView):
    template_name = "jacked/macros.html"

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        form = MacroForm()
        return render(request, self.template_name, {'form': form})
