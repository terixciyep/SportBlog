
from django.shortcuts import render
from django.views.generic import ListView
from sportsman.models import Sportsman_user
from user_ranks.models import UserRank


class UserRanksListView(ListView):
    model = Sportsman_user
    paginate_by = 10
    template_name = 'user_ranks/users_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = self.object_list.all()
        return context


class RanksView(ListView):
    model = UserRank
    template_name = 'user_ranks/user_ranks_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_ranks'] = self.object_list.all()
        return context