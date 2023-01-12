from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..models import *


def ArchivedPosts(request):
    return render(request, "dashboard/posts/videos.html")