from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Post, Comment
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'name','avatar','info']

class CreatePostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ['title','text']


class CreateCommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ['text']



