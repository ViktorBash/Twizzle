from django.shortcuts import render, get_object_or_404
from .models import Board, Items
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, 'todoboard/home.html')


class HomeView(ListView, UserPassesTestMixin):
    model = Board
    template_name = "todoboard/home.html"
    context_object_name = "boards"
    ordering = ['-date_posted']

    # def test_func(self):
    #     board = self.get_object()
    #     if self.request.user == board.author:
    #         return True
    #     return False

    def get_queryset(self):
        return Board.objects.all().filter(author=self.request.user)

    # def get_context_data(self, **kwargs):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #
    #     context = super(HomeView, self).get_context_data(**kwargs)
    #     context['board'] = Board.objects.filter(author=user).order_by
    #     return context

    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     return Board.objects.filter(author=user).order_by('-date_posted')

