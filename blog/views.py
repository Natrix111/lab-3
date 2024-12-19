from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.views import LoginView
from .forms import CreateUserForm, CreatePostForm, CreateCommentForm
from django.urls import reverse_lazy
from .models import Post, Comment, User

class index(generic.ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 50

class SignUp(generic.CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy('index')
    template_name = 'register/register.html'

class Login(LoginView):
    template_name = 'register/login.html'

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def profile(request):
    return render(request, 'profile.html')

class UpdateProfile(LoginRequiredMixin, generic.UpdateView):
    model = User
    success_url = reverse_lazy('profile')
    template_name = 'register/update.html'
    fields = ['name','avatar','info']

class UserDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = User
    template_name = 'deleteuser.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user


class CreatePost(LoginRequiredMixin, generic.CreateView):
    form_class = CreatePostForm
    success_url = reverse_lazy('index')
    template_name = 'createpost.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DetailPost(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments_list'] = self.object.comment_set.all()
        return context

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('index')

class CreateComment(LoginRequiredMixin, generic.CreateView):
    form_class = CreateCommentForm
    success_url = reverse_lazy('index')
    template_name = "createcomment.html"

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdateComment(LoginRequiredMixin, generic.UpdateView):
    model = Comment
    success_url = reverse_lazy('index')
    template_name = 'updatecomment.html'
    fields = ['text']

class DeleteComment(LoginRequiredMixin, generic.DeleteView):
    model = Comment
    success_url = reverse_lazy('index')
    template_name = 'deletecomment.html'

@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post', pk=pk)