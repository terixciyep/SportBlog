from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.core.exceptions import ValidationError

from sportsman.utils import send_mail_for_verify

User = get_user_model()


class UserCreationForm(UserCreationForm):


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email",)


class AuthForm(AuthenticationForm):

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
            if not self.user_cache.email_verify:
                send_mail_for_verify(self.request, self.user_cache)
                raise ValidationError(
                    'Email not verify, check your email',
                    code='invalid_login',
                )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data
    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(self.request, email=email, password=password)
        if user is not None and user.email_verify == True:
            login(self.request, user)
            raise ValueError(f"{user.email_verify}")
            return super().form_valid(form)
        else:
            # Обработка неверных данных для входа
            return self.form_invalid(form)