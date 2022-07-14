from django.shortcuts import render, get_list_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Categorie
# from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.db import connection
from .tools import get_who_liked_this_post
# Create your views here.

def LikeView(request, pk):
    # post = get_list_or_404(Post, id=request.POST.get('post_id'))
    post = Post.objects.get(id=pk)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse_lazy('post_detail', args=[str(pk)]))


class HomeView(ListView):
    model=Post
    template_name='home.html'
    ordering=['-post_date']
    def get_context_data(self,*args, **kwargs):
        cat_menu = Categorie.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class PostDetailView(DetailView):
    model=Post
    template_name='post_detail.html'
    def get_context_data(self,*args, **kwargs):
        cat_menu = Categorie.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        
        stuff =  Post.objects.get(id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        who = get_who_liked_this_post(self.kwargs['pk'])
        context['who_liked'] = who
        context["liked"] = liked
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        return context
def CategoryView(request, cats):
    category_posts=Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts': category_posts })

class PostCreateView(CreateView):
    model=Post
    # form_class = PostForm
    template_name='post_new.html'
    # fields="__all__"
    def get_context_data(self,*args, **kwargs):
        cat_menu = Categorie.objects.all()
        context = super(PostCreateView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
class CategoryCreateView(CreateView):
    model=Categorie
    template_name='category_new.html'
    fields="__all__"
    def get_context_data(self,*args, **kwargs):
        cat_menu = Categorie.objects.all()
        context = super(CategoryCreateView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
class PostUpdateView(UpdateView):
    model=Post
    template_name='update_post.html'
    # form_class = EditForm
    def get_context_data(self,*args, **kwargs):
        cat_menu = Categorie.objects.all()
        context = super(PostUpdateView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
class PostDeleteView(DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url = reverse_lazy('home')
    def get_context_data(self,*args, **kwargs):
        cat_menu = Categorie.objects.all()
        context = super(PostDeleteView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context









