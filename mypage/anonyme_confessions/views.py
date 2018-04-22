from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Article, User, Comment
from .forms import AddArticleForm, LoginForm, RegistrationForm, CommentingForm
import pytz
from datetime import datetime, time
from django.shortcuts import redirect
from .pass_test import Pass_test


def index(request):
    if request.session.get('member_nick', False):
        logged = True
        latest_article_list = Article.objects.order_by('-pub_date')[:10]
        now = datetime.now(pytz.utc)
        comment = Comment.objects.order_by('com_date').reverse()
        context = {'latest_article_list': latest_article_list, 'logged': logged, 'now': now, 'comment': comment}
    else:
        latest_article_list = Article.objects.order_by('-pub_date')[:10]
        now = datetime.now(pytz.utc)
        comment = Comment.objects.order_by('com_date').reverse()
        context = {'latest_article_list': latest_article_list, 'now': now, 'comment': comment}
    return render(request, 'anonyme_confessions/index.html', context)



def articles_id(request, articles_id):
    form = CommentingForm()
    article = Article.objects.get(pk=articles_id)
    comment = Comment.objects.filter(article_id=articles_id).order_by('com_date').reverse()
    now = datetime.now(pytz.utc)
    if request.session.get('member_nick', False):
        logged = True
        context = {'article': article, 'comment': comment, 'logged': logged, 'now': now, 'form': form}
    else:
        context = {'article': article, 'comment': comment, 'now': now, 'form': form}
    if request.session.get('member_nick', False):
        if request.method == 'POST':
            form = CommentingForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.article_id = article
                post.commentator_nick = request.session.get('member_nick')
                post.comment = form.cleaned_data.get('comment')
                post.com_date = datetime.now(pytz.utc)
                post.save()
                return redirect('../', pk=post.pk)
    else:
        if request.method == 'POST':
            form = CommentingForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.commentator_nick = 'Gość'
                post.article_id = article
                post.comment = form.cleaned_data.get('comment')
                post.com_date = datetime.now(pytz.utc)
                post.save()
                return redirect('../', pk=post.pk)
    return render(request, 'anonyme_confessions/article.html', context)

def add_article(request):
    if request.session.get('member_nick', False):
        if request.method == 'POST':
            form = AddArticleForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                username = request.session.get('member_nick')
                user = User.objects.get(pk=username)
                post.username = user
                post.title = form.cleaned_data.get('title')
                post.content = form.cleaned_data.get('content')
                post.keywords = form.cleaned_data.get('keywords')
                post.pub_date = datetime.now(pytz.utc)
                post.save()
                return redirect('../', pk=post.pk)
        else:
            form = AddArticleForm()
    else:
        return redirect('login_view')
    if request.session.get('member_nick', False):
        logged = True
        return render(request, 'anonyme_confessions/add_article.html', {'form': form, 'logged': logged})
    else:
        return render(request, 'anonyme_confessions/add_article.html', {'form': form})




def register_view(request):
    form = RegistrationForm()
    if request.method == 'POST':
        post = form.save(commit=False)
        post.username = request.POST.get('username')
        post.password = request.POST.get('password')
        post.confirm_password = request.POST.get('confirm_password')
        try:
            user_name = User.objects.get(pk=post.username).username
            return HttpResponse('Login zajęty')
        except User.DoesNotExist:
            pw = post.password
            if len(post.username) >= 6:
                if ( Pass_test.test_password1(pw) or Pass_test.test_password2(pw) ) and post.password != post.username and post.password == post.confirm_password:
                    post.save()
                    return redirect('login_view')
                else:
                    return HttpResponse('Podane hasło jest zbyt słabe, lub hasła się nie zgadzają')
            else:
                return HttpResponse('Nazwa użytkownika musi mieć co najmniej 6 znaków')
    return render(request, 'anonyme_confessions/register.html', {'form': form})

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_name = User.objects.get(pk=username).username
        pass_word = User.objects.get(pk=username).password
        if user_name == username and password == pass_word:
            request.session['member_nick'] = username
            return redirect('../')
        else:
            return HttpResponse('Niestety coś poszło nie tak')
    return render(request, 'anonyme_confessions/login.html', {'form': form})

def logout(request):
    try:
        del request.session['member_nick']
    except KeyError:
        pass
    return redirect('../')