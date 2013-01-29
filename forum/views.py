# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib import messages
from forum.form import UserCreateForm, NewPostForm
from forum.models import Post
from taggit.models import Tag

import datetime
def index(request):
    announcements = Post.objects.filter(announcement=1,status=1).order_by('-publish_at')
    posts = Post.objects.filter(announcement=0, status=1)
    return render_to_response('discussion/index.html',{'announcements':announcements, 'posts':posts},context_instance=RequestContext(request))

@login_required
def new_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if 'new_post' in request.POST:
                post.status = 1
            elif 'draft' in request.POST:
                post.status = 0
            post.save()
            form.save_m2m()
            messages.success(request, 'Posted successfully')

            return HttpResponseRedirect(reverse('forum:index'))
        else:
            messages.error(request, 'Posted failed, please check it again')
    else:
        form = NewPostForm()
    return render_to_response('discussion/new_post.html',{'form':form},context_instance=RequestContext(request))

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Register Successfully")
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            if user is not None:
                if user.is_active:
                    login(request, user)
            return HttpResponseRedirect(reverse('forum:index'))
    else:
        form = UserCreateForm()

    return render_to_response('discussion/register.html',{'form':form},context_instance=RequestContext(request))

def category_post_list(request, category_id):
    announcements = Post.objects.filter(announcement=1,status=1).order_by('-publish_at')
    post_list = Post.objects.filter(category__id=category_id, status=1,announcement=0)
    post_list = post_list.order_by('-publish_at')

    return render_to_response('discussion/index.html', {'announcements':announcements,'posts':post_list},context_instance=RequestContext(request))

def tag_post_list(request, tag_name):
    announcements = Post.objects.filter(tags__name=tag_name,announcement=1,status=1).order_by('-publish_at')
    post_list = Post.objects.filter(tags__name=tag_name,announcement=0,status=1).order_by('-publish_at')

    return render_to_response('discussion/index.html', {'announcements':announcements,'posts':post_list},context_instance=RequestContext(request))

def post(request, post_id):
    post_entry = get_object_or_404(Post, pk=post_id)

    post_entry.num_views += 1
    post_entry.save()
    return render_to_response('discussion/post.html', {'post':post_entry},context_instance=RequestContext(request))

def post_show_comment(request, id=''):
    post = Post.objects.get(id=id)
    return render_to_response('discussion/post_comment_show.html', {"post": post})

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'Logout Successfully ')
    return HttpResponseRedirect(reverse('forum:index'))