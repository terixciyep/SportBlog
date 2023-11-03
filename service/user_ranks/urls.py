from django.conf.urls.static import static
from django.urls import path

from service import settings
from user_ranks import views
app_name = 'user_ranks'

urlpatterns = [
    path('users/', views.UserRanksListView.as_view(), name='users_ranks_list'),
    path('users/<int:pk>', views.RanksView.as_view(), name='users_ranks_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)