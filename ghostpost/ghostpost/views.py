from django.shortcuts import render, HttpResponseRedirect, get_object_or_404

from .models import Post
from .forms import PostForm


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = PostForm()
    return render(request, "add_post.html", {"form": form})


def index(request):
    latest_post_list = Post.objects.order_by("pub_date")
    context = {"latest_post_list": latest_post_list}
    return render(request, "index.html", context)


def sort_by_votes(request):
    latest_post_list = Post.objects.order_by("-votes")
    context = {"latest_post_list": latest_post_list}
    return render(request, "index.html", context)


def sort_by_boast(request):
    boast_post_list = Post.objects.filter(boast=True)
    context = {"boast_post_list": boast_post_list}
    return render(request, "index.html", context)


def sort_by_roast(request):
    roast_post_list = Post.objects.filter(boast=False)
    context = {"roast_post_list": roast_post_list}
    return render(request, "index.html", context)


def upvote(request, post_id):
    latest_post_list = Post.objects.order_by("pub_date")
    context = {"latest_post_list": latest_post_list}
    post = get_object_or_404(Post, pk=post_id)
    post.votes += 1
    post.save()
    return render(request, "index.html", context)


def downvote(request, post_id):
    latest_post_list = Post.objects.order_by("pub_date")
    context = {"latest_post_list": latest_post_list}
    post = get_object_or_404(Post, pk=post_id)
    post.votes -= 1
    post.save()
    return render(request, "index.html", context)
