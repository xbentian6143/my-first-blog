from django.shortcuts import render, redirect
from .models import User,Connection
from django.contrib.auth import login, authenticate, get_user_model
from django.views.generic import CreateView
from . forms import LoginForm,ProfileForm
import sys
sys.path.append('../')
from post.models import Post,Idea,Sympathy,Good
from rest_framework import viewsets
from django.views.generic import CreateView,View, TemplateView, DetailView, UpdateView, ListView
from . forms import UserCreationForm,UserChangeForm,UserPasswordChangeForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.template.response import TemplateResponse
from django.shortcuts import render,get_object_or_404
from django.utils.timezone import make_aware
from django.utils import timezone
import datetime
# Create your views here.


# Create your views here.

   



def profile(request):
    posts = Post.objects.filter(author=request.user).order_by('-published_date')
    ideas = Idea.objects.filter(author=request.user).order_by('-published_date')
    profile_followees = Connection.objects.filter(followed_user = request.user)
    profile_followees_count = profile_followees.count()
    #フォローワ―
    profile_followers = Connection.objects.filter(followed_target = request.user )
    profile_followers_count = profile_followers.count()
    good_list = Good.objects.filter(user = request.user )
    good_idea_list = [good.target for good in good_list ]
    sympathy_list = Sympathy.objects.filter(user = request.user)
    sympathy_post_list = [sympathy.target for sympathy in sympathy_list]
    
    return render(request, 'accounts/profile.html', 
        {'posts':posts,
        'ideas':ideas,
        'profile_followees': profile_followees,
        'profile_followers': profile_followers,
        'profile_followees_count': profile_followees_count,
        'profile_followers_count': profile_followers_count,
        'good_idea_list':good_idea_list,
        'sympathy_post_list':sympathy_post_list
        })
    

def user_profile(request,user_pk):
    profile_user = User.objects.get(pk=user_pk)

    posts = Post.objects.filter(author=profile_user).order_by('-published_date')
    ideas = Idea.objects.filter(author=profile_user).order_by('-published_date')
    profile_followees = Connection.objects.filter(followed_user = profile_user)
    profile_followees_count = profile_followees.count()
    #フォローワ―
    profile_followers = Connection.objects.filter(followed_target = profile_user )
    profile_followers_count = profile_followers.count()
    good_list = Good.objects.filter(user = request.user )
    good_idea_list = [good.target for good in good_list ]
    sympathy_list = Sympathy.objects.filter(user = request.user)
    sympathy_post_list = [sympathy.target for sympathy in sympathy_list]
    print(user_pk)
    print(profile_user)

    return TemplateResponse(request, 'accounts/user_profile.html',
        {'profile_user': profile_user,
        'posts':posts,
        'ideas':ideas,
        'profile_followees': profile_followees,
        'profile_followers': profile_followers,
        'profile_followees_count': profile_followees_count,
        'profile_followers_count': profile_followers_count,
        'good_idea_list':good_idea_list,
        'sympathy_post_list':sympathy_post_list
         })

 
@login_required 
def follow(request,user_pk):
    """フォローボタンをクリック"""
    if request.method == 'POST':
        query = Connection.objects.filter(followed_user = request.user, followed_target=get_object_or_404(User, pk=user_pk))
        if query.count() == 0:
            connection = Connection()
            connection.followed_user  = request.user
            connection.followed_target = get_object_or_404(User, pk=user_pk)
            connection.created_date = make_aware(datetime.datetime.now())
            connection.save()

        else:
            query.delete()

    return redirect ('accounts:user_profile', user_pk=user_pk)   


  







#アカウント作成
class Create_account(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            #フォームから'username'を読み取る
            username = form.cleaned_data.get('username')
            #フォームから'password1'を読み取る
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'accounts/create.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        return  render(request, 'accounts/create.html', {'form': form,})

create_account = Create_account.as_view()


#ログイン機能
class Account_login(View):
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('/')
        return render(request, 'registration/login.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'registration/login.html', {'form': form,})

account_login = Account_login.as_view()

#アカウント情報変更機能
@login_required
def change_data(request):
 
    form = UserChangeForm(request.POST or None, instance=request.user)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("accounts:profile")
 
    context = {
        "form": form,
    }
    return render(request, 'accounts/change_data.html', context)


class ProfileEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_data = User.objects.get(id=request.user.id)
        form = ProfileForm(
            request.POST or None,
            initial={
                'nickname': user_data.nickname,
                'introduction': user_data.introduction,
                'icon': user_data.icon
            }
        )

        return render(request, 'accounts/profile_edit.html', {
            'form': form,
            'user_data': user_data
        })

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            user_data = User.objects.get(id=request.user.id)
            
            user_data.nickname = form.cleaned_data['nickname']
            user_data.introduction = form.cleaned_data['introduction']
            if request.FILES.get('icon'):
                user_data.icon = request.FILES.get('icon')
            user_data.save()
            return redirect('accounts:profile')

        return render(request, 'accounts/profile.html', {
            'form': form
        })



@login_required
def change_password(request):
 
    form = UserPasswordChangeForm(request.user, request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("accounts:profile")
 
    context = {
        "form": form,
    }
    return render(request, 'registration/password_change_form.html', context)


class PasswordReset(PasswordResetView):
    """パスワード変更用URLの送付ページ"""
    subject_template_name = 'registration/mail_template/reset/subject.txt'
    email_template_name = 'registration/mail_template/reset/message.txt'
    template_name = 'registration/password_reset_form.html'
    success_url = reverse_lazy('accounts:password_reset_done')


class PasswordResetDone(PasswordResetDoneView):
    """パスワード変更用URLを送りましたページ"""
    template_name = 'registration/password_reset_done.html'


class PasswordResetConfirm(PasswordResetConfirmView):
    """新パスワード入力ページ"""
    success_url = reverse_lazy('accounts:password_reset_complete')
    template_name = 'registration/password_reset_confirm.html'


class PasswordResetComplete(PasswordResetCompleteView):
    """新パスワード設定しましたページ"""
    template_name = 'registration/password_reset_complete.html'
