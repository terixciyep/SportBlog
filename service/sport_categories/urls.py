from django.conf.urls.static import static
from django.urls import path

from service import settings
from sport_categories import views
app_name = 'sport_categories'

urlpatterns = [
    path('',views.SportsListView.as_view(), name='sport'),
    path('category/<int:pk>', views.SportView.as_view(), name='category'),
    path('exercises/<int:pk>', views.ExerciseListView.as_view(), name='exercises'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)