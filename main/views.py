from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post,Comment
from .forms import Commented
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin 
)


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'



class homePageView(ListView):
    model = Post
    template_name = 'index.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'detail.html'


class BlogCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'nextpage'
    model = Post
    template_name = 'post.html'
    fields = ['title', 'body']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'nextpage'
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    login_url = '/accounts/login/'
    redirect_field_name = 'nextpage'

    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user



@login_required
def dashboard(request):
    user = request.user
    return render(request, 'dashboard.html', {'user':user})



        