from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm
from django.utils.timezone import now
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from gallery.views import carusel


def index(request):
    posts = Post.objects.all().order_by("-published_date")
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {"posts": posts}
    context.update(carusel())
    return render(request, "blog/index.html", context)


def get_comments(id=None):
    comments = Comment.objects.filter(post=id).order_by("-published_date")
    context = {"comments": comments}
    return context


def post(request, id=None):
    p = get_object_or_404(Post, pk=id)
    context = {"post": p}
    context.update(get_comments(id))
    context.update(carusel())
    return render(request, "blog/post.html", context)


def comment(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.published_date = now()
            p.post = post
            p.save()
            return redirect("post", id=post.pk)
    else:
        form = CommentForm()
    return render(request, "blog/comment.html", {"form": form})