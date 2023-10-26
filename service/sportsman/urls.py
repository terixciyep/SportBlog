from django.urls import path, include

from sportsman import views

app_name='sportsman'

urlpatterns = [
    path("login/", views.LoginViewApp.as_view(), name="login"),
    path('', include('django.contrib.auth.urls')),
    path('register/',views.Register.as_view(), name='register'),
    path('',views.get_index, name='get_index'),
]