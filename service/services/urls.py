from django.urls import path
from services import views
app_name = 'service'

urlpatterns = [
    path('',views.index, name='index'),
]