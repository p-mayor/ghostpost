from django.shortcuts import render, HttpResponseRedirect

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
    latest_post_list = Post.objects.order_by('pub_date')
    context = {'latest_post_list': latest_post_list}
    return render(request, 'index.html', context)


# def sort_by_likes(request):

# def sort_by_likes_reverse(request):

def sort_by_boast(request):
    boast_post_list = Post.objects.filter(boast=True)
    context = {'boast_post_list': boast_post_list}
    return render(request, 'index.html', context)

def sort_by_roast(request):
    roast_post_list = Post.objects.filter(boast=False)
    context = {'roast_post_list': roast_post_list}
    return render(request, 'index.html', context)

def upvote(request):
    return render(request, 'index.html')

def downvote(request):
    return render(request, 'index.html')
