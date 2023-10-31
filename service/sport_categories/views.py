from django.shortcuts import render
from django.views.generic import ListView, DetailView
from sport_categories.models import Sport, Exercise

class SportsListView(ListView):
    model = Sport
    paginate_by = 5
    template_name = 'sport_categories/sport_categories.html'


class SportView(DetailView):
    model = Sport
    template_name = 'sport_categories/category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sport = Sport.objects.get(pk=self.object.id)
        exercises = sport.exercises.all()
        context['exercises'] = exercises
        context['sport'] = sport
        return context


class ExerciseListView(DetailView):
    model = Exercise
    template_name = 'sport_categories/exercise.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exercise = Exercise.objects.get(pk=self.object.id)
        ranks = exercise.ranks.all()
        context['exercise'] = exercise
        context['ranks'] = ranks
        return context