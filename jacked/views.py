from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, CreateView, View
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse

from .models import MacroCycle, MesoCycle
from .forms import MacroForm, MesoForm
# Create your views here.

class Home(TemplateView):
    template_name = 'jacked/front_page.html'

    def get(self, request):
        users = User.objects.all()
        return render(request, self.template_name, {'users': users})

class MacroCyclesView(View):
    form = MacroForm

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')

        macros = MacroCycle.objects.filter(user=user_id)
        return render(request, "jacked/macros.html", {'form': self.form(), 'macros': macros})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        form_input = self.form(request.POST)
        if form_input.is_valid():
            f = form_input.save(commit=False)
            f.user = request.user
            f.save()
            messages.success(request, 'Form valid')
        else:
            messages.error(request, 'Form invalid')
        return redirect(reverse('jacked:macros', args=[user_id]))
        return render(request, "jacked/macros.html", {'form': form(), 'macros': macros})



#Todo: meso cycles now showing up. This is because you never query them. Find somthing smart
class MacroCycleView(View):
    form = MesoForm

    def get(self, request, *args, **kwargs):
        macro_id = kwargs.get('macro_id')
        macro = MacroCycle.objects.get(id=macro_id)
        meso = MesoCycle.objects.filter(macro_id=macro_id)

        return render(request, 'jacked/macro.html', {'macro': macro, 'meso': meso, 'form': self.form()})

    def post(self, request, *args, **kwargs):
        macro_id = kwargs.get('macro_id')

        form_input = self.form(request.POST)
        if form_input.is_valid():
            f = form_input.save(commit=False)
            f.macro_id = MacroCycle.objects.get(pk=macro_id)
            f.save()
            messages.success(request, 'Form valid')
        else:
            messages.error(request, 'Form invalid')
            return redirect(reverse('jacked:macro', args=[macro_id]))
        return render(request, 'jacked/macro.html', {'macro': macro, 'meso': mesos, 'form': self.form()})
