from django.conf.urls.static import static
from django.urls import path, include

from service import settings
from sportsman import views

app_name = 'sportsman'

urlpatterns = [
    path('reset_password', views.ResetPasswordViewApp.as_view(), name='reset_password'),
    path("password_reset/done/",views.PasswordResetDoneViewApp.as_view(),name="password_reset_done",),
    path("reset/<uidb64>/<token>/",views.PasswordResetConfirmViewApp.as_view(),name="password_reset_confirm",),
    path("reset/done/",views.PasswordResetCompleteViewApp.as_view(),name="password_reset_complete",),
    path("login/", views.LoginViewApp.as_view(), name="login"),
    path('verify_email/<uidb64>/<token>/',views.EmailVerifyView.as_view(),name='verify_email'),
    path('', include('django.contrib.auth.urls')),
    path('register/',views.Register.as_view(), name='register'),
    path('profile/',views.ProfileView.as_view(), name='profile')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)