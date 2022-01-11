from django.shortcuts import render
from .models import Post, Comment
from .form import CommentForm
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
# Create your views here.
class PostListView(ListView):
   queryset = Post.objects.all().order_by('-date')
   template_name = 'blog/blog.html'
   context_object_name = 'Posts'
   paginate_by = 10
# Create your views here.
class PostDetailView(DetailView):
    try:
       model = Post
       template_name = 'blog/post.html'
    except Post.DoesNotExist:
        raise Http404("Bài viết không tồn tại")

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "blog/post.html", {"post": post, "form": form})
    