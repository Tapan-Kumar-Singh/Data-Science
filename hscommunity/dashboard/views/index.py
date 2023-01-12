from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..models import *


def index(request):
    return render(request, "dashboard/welcome/index.html")
