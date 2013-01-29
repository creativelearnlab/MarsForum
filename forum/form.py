__author__ = 'jxl'
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, ChoiceField
from forum.models import Post

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class NewPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category','content','tags')
        widgets = {
            'title': forms.TextInput(attrs={'class':'InputBox BigInput', 'id':'Form_Name'}),
            'category' : forms.Select(attrs={'id':"Form_CategoryID"}),
            'content':forms.Textarea(attrs={'id':"Form_Body", 'rows':6, 'cols':"100", 'class':"TextBox", 'style':"overflow: hidden; display: block;"}),
            'tags':forms.TextInput(attrs={'id':"Form_Tags", 'maxlength':255, 'class':"InputBox"})
        }