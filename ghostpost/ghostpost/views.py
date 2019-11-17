from django.shortcuts import render, HttpResponseRedirect

from .models import Post
from .forms import PostForm


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form':form})
   

def homepage(request):
    return render(request, 'homepage.html')


# def sort_by_likes(request):

# def sort_by_likes_reverse(request):

# def sort_by_boast(request):

# def sort_by_roast(request):

# def boast(request):

# def roast(request):

# def add_like(request):

# def remove_like(request):
