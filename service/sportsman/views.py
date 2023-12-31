from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetCompleteView
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
from django.views import View
import django.contrib.auth.urls
from django.views.generic import DetailView

from sportsman.forms import UserCreationForm, AuthForm, PasswordResetFormCustom, ProfileForm
from sportsman.models import Sportsman_user
from django.contrib.auth.tokens import default_token_generator as token_generator

from sportsman.utils import send_mail_for_verify


# Create your views here.

class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm(),
            'title': 'Регистрация'
        }
        if request.user.is_authenticated:
            return redirect(reverse_lazy('service:index'))
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if request.user.is_authenticated:
            return redirect(reverse_lazy('service:index'))
        if form.is_valid():
            form.save()
            user = authenticate(email=form.cleaned_data['em ail'],password=form.cleaned_data['password1'])
            send_mail_for_verify(request,user)
            return redirect(reverse_lazy('sportsman:login'))
        else:
            return render(request, self.template_name, context={'form': form,'title':'Регистрация'})


class LoginViewApp(LoginView):
    form_class = AuthForm
    template_name = "registration/login.html"
    redirect_authenticated_user = True
    extra_context = {'title':'Вход в профиль'}

class EmailVerifyView(View):
    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect(reverse_lazy('sportsman:login'))
        return redirect('sportsman:register')

    @staticmethod
    def get_user(uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = Sportsman_user.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError,
                Sportsman_user.DoesNotExist, ValidationError):
            user = None
        return user

class ResetPasswordViewApp(PasswordResetView):
    template_name = 'sportsman/reset_password.html'
    success_url = reverse_lazy("sportsman:password_reset_done")
    email_template_name = 'registration/html_form_email.html'
    form_class = PasswordResetFormCustom
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse_lazy('sport_categories:sport'))
        return super().dispatch(*args, **kwargs)
class PasswordResetDoneViewApp(PasswordResetDoneView):
    template_name = "sportsman/reset_password_done.html"
    title = "Password reset sent"
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse_lazy('sport_categories:sport'))
        return super().dispatch(*args, **kwargs)

class PasswordResetConfirmViewApp(PasswordResetConfirmView):
    success_url = reverse_lazy("sportsman:password_reset_complete")
    template_name = "sportsman/reset_password_confirm.html"
    title = "Enter new password"

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse_lazy('sport_categories:sport'))
        return super().dispatch(*args, **kwargs)
class PasswordResetCompleteViewApp(PasswordResetCompleteView):
    template_name = "sportsman/reset_password_complete.html"
    title = "Password reset complete"

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse_lazy('sport_categories:sport'))
        return super().dispatch(*args, **kwargs)

class ProfileView(View):
    def get(self, request):
        if request.user.is_authenticated:
            form = ProfileForm(instance=request.user)
            context = {'form':form}
            return render(request, 'sportsman/profile.html',context=context)
        else:
            return redirect(reverse_lazy('sportsman:login'))
    def post(self, request):
        if request.user.is_authenticated:
            instance = request.user
            form = ProfileForm(instance=instance,data=request.POST)
            if form.is_valid():
                if request.POST['password']:
                    request.user.set_password(request.POST['password'])
                form.save()
                context = {'form': form}
                return render(request, 'sportsman/profile.html', context=context)
            else:
                context = {'form':form}
                return render(request, 'sportsman/profile.html', context=context)
        else:
            return redirect(reverse_lazy('sportsman:login'))
def main_page(request):
    return render(request, 'sportsman/index.html')