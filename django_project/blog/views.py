from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# class based views
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts' # to change the defaul name which is object to posts
    ordering = ['-date_posted']
    paginate_by = 1

# post by a specific author
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    # filters the post that belongs to the logged in user
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post # it calls object in the template
    # used the default template name
    # automatically has 404

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # sets the author to the current logged in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # go to models to configure something

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # sets the author to the current logged in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # checks if the current logged in user is the author of the post, throws a 403 error
    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post 
    success_url = '/' # sends back to home page after successfully deleting the post

    # checks if the current logged in user is the author of the post
    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True