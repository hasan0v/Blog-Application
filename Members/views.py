from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import EditProfileForm, SignUpForm, PasswordChangingForm
from BlogApp.models import Profile
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from BlogApp.tools import user_profile_checker, get_followers, get_follows, get_liked_posts, get_user_posts


# Create your views here.
def FollowerView(request, pk):
    user = Profile.objects.get(id=pk)

    follow = False
    if user.follower.filter(id=request.user.id).exists():
        user.follower.remove(request.user)
        follow = False
    else:
        user.follower.add(request.user)
        follow =True

    return HttpResponseRedirect(reverse_lazy('show_profile_page', args=[str(pk)]))


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
    def get_context_data(self,*args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        stuff =  Profile.objects.get(id=self.kwargs['pk'])
        total_follower = stuff.total_follower()
        
        follower = False
        if stuff.follower.filter(id=self.request.user.id).exists():
            follower = True
        
        follow = False
        
        user = user_profile_checker(self.kwargs['pk'])
        if user == self.request.user.id:
            context["myself"] = False
        else:
            context["myself"] = True
        
        followers = get_followers(self.kwargs['pk'])
        follows = get_follows(self.kwargs['pk'])
        liked_posts = get_liked_posts(self.kwargs['pk'])
        user_posts = get_user_posts(self.kwargs['pk'])

        context["liked_posts"] = liked_posts
        context["count_liked_posts"] = len(liked_posts)
        context["user_posts"] = user_posts
        context["count_user_posts"] = len(user_posts)
        context["follows"] = follows
        context["count_follows"] = len(follows)
        context["count_followers"] = len(followers)
        context["followers"] = followers
        context["follower"] = follower
        context["total_follower"] = total_follower
        return context

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'prof_pic']
    success_url  = reverse_lazy('home')

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'registration/change-password.html'
    success_url  = reverse_lazy('password_success')
def password_success(request):
    return render(request, 'registration/password_success.html')

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url  = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url  = reverse_lazy('home')

    def get_object(self):
        return self.request.user
