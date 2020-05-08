from django.shortcuts import render, get_object_or_404, redirect
from .models import Board, Items, Shared_User
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse

# Old home view
# def home(request):
#     return render(request, 'todoboard/home.html')


class HomeView(ListView, UserPassesTestMixin):
    model = Board
    template_name = "todoboard/home.html"
    context_object_name = "boards"
    ordering = ['-date_posted']

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return None
        return Board.objects.all().filter(author=self.request.user)


class BoardDetail(DetailView, LoginRequiredMixin):
    model = Board
    template_name = "todoboard/board_detail.html"
    context_object_name = "boards"

    # def test_func(self):
    #     board = self.get_object()
    #     if self.request.user == board.author:
    #         return True
    #     return False

    def get_context_data(self, **kwargs):
        specific_board = self.get_object()
        context = super(BoardDetail, self).get_context_data(**kwargs)
        context['items'] = Items.objects.filter(board=specific_board)
        shared_user_info = Shared_User.objects.filter(board=specific_board)
        context['shared_users'] = shared_user_info
        # print(context['shared_users'])
        # print(context)
        return context


def delete_item(request, pk, itempk):
    Items.objects.get(pk=itempk).delete()
    return_link = "/board/" + str(pk) + "/"

    return redirect(return_link)


def create_board(request):
    title = request.POST['title']
    created_board = Board.objects.create(title=title, author=request.user)
    return HttpResponseRedirect("/")


def create_item(request, pk):
    title = request.POST['title']
    content = request.POST['content']

    created_item = Items.objects.create(title=title, author=request.user, board_id=pk, content=content)

    return_link = "/board/" + str(pk) + "/"
    return redirect(return_link)


class BoardDelete(LoginRequiredMixin, DeleteView, UserPassesTestMixin):
    model = Board
    success_url = "/"

    def test_func(self):
        board = self.get_object()
        if self.request.user == board.author:
            return True
        return False


def BoardAddUser(request, pk):
    shared_user = request.POST['shared_user']
    created_shared_user = Shared_User.objects.create(board_id=pk, shared_author=shared_user)
    return_link = "/board/" + str(pk) + "/"
    return redirect(return_link)

