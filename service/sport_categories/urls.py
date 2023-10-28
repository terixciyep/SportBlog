from django.urls import path
from services import views

app_name = 'sport_categories'

urlpatterns = [
    path('',views.CategoriesView.as_view(), name='caregories'),
]