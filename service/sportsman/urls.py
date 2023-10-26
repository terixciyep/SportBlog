from django.urls import path, include


app_name='sportsman'

urlpatterns = [
    path('', include('django.contrib.auth.urls'))
]