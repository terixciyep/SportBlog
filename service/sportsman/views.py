from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetCompleteView
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
from django.views import View
import django.contrib.auth.urls
from sportsman.forms import UserCreationForm, AuthForm
from sportsman.models import Sportsman_user
from django.contrib.auth.tokens import default_token_generator as token_generator

from sportsman.utils import send_mail_for_verify


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
            user = authenticate(email=form.cleaned_data['email'],password=form.cleaned_data['password1'])
            send_mail_for_verify(request,user)
            return redirect(reverse_lazy('sportsman:login'))
        else:
            return render(request, self.template_name, context={'form': form})


class LoginViewApp(LoginView):
    form_class = AuthForm
    template_name = "registration/login.html"
    redirect_authenticated_user = True
    extra_context = None

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

class PasswordResetDoneViewApp(PasswordResetDoneView):
    template_name = "sportsman/reset_password_done.html"
    title = "Password reset sent"


class PasswordResetConfirmViewApp(PasswordResetConfirmView):
    success_url = reverse_lazy("sportsman:password_reset_complete")
    template_name = "sportsman/reset_password_confirm.html"
    title = "Enter new password"

class PasswordResetCompleteViewApp(PasswordResetCompleteView):
    template_name = "sportsman/reset_password_complete.html"
    title = "Password reset complete"

def get_index(request):
    return render(request, 'sportsman/index.html')
