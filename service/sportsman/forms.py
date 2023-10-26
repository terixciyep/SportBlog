from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

User = get_user_model()


class UserCreationForm(UserCreationForm):


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email",)


class AuthForm(AuthenticationForm):
    email = forms.EmailField()

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(self.request, email=email, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            # Обработка неверных данных для входа
            return self.form_invalid(form)