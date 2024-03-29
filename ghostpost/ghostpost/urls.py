"""ghostpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from ghostpost.models import Post

admin.site.register(Post)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("upvote/<int:post_id>/", views.upvote, name="upvote"),
    path("downvote/<int:post_id>/", views.downvote, name="downvote"),
    path("votesort", views.sort_by_votes, name="votesort"),
    path("filterboast/", views.sort_by_boast, name="boast_list"),
    path("filterroast/", views.sort_by_roast, name="roast_list"),
    path("add_post/", views.add_post, name="add_post"),
    path("", views.index, name="homepage"),
]
