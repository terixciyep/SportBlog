from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
import django.contrib.auth.urls
from sportsman.forms import UserCreationForm, AuthForm


# Create your views here.

class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        if request.user.is_authenticated:
            return redirect(reverse_lazy('service:index'))
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('sportsman:login'))
        else:
            return render(request, self.template_name, context={'form': form})


class LoginViewApp(LoginView):
    form_class = AuthForm
    template_name = "registration/login.html"
    redirect_authenticated_user = True
    extra_context = None


def get_index(request):
    return render(request, 'sportsman/index.html')
