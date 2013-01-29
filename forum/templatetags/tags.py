__author__ = 'jxl'
from django.template import  Library
from forum.form import UserCreateForm
from django.contrib.auth.forms import AuthenticationForm
from forum.models import Category, Post

register = Library()

@register.inclusion_tag('tags/register_tags.html')
def user_register():
    form = UserCreateForm()
    return {'form':form}

@register.inclusion_tag('tags/login_tags.html')
def user_login():
    form = AuthenticationForm()
    return {'form':form}

@register.inclusion_tag('tags/category.html')
def category():
    category = Category.objects.all()
    return {'category_list' : category}

@register.inclusion_tag('tags/recent_post.html')
def recent_post():
    posts = Post.objects.order_by('-publish_at')[:8]
    return  {'posts':posts}