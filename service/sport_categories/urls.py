from django.urls import path
from sport_categories import views
app_name = 'sport_categories'

urlpatterns = [
    path('',views.SportsListView.as_view(), name='sport'),
    path('category/<int:pk>', views.SportView.as_view(), name='category'),
    path('exercises/<int:pk>', views.ExerciseListView.as_view(), name='exercises')

]