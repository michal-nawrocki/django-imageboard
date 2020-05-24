from django.shortcuts import render
from django.http import HttpResponse

from .models import Thread, Post


def index(request):
    latest_threads = Thread.objects.order_by("-creation_datetime")[:5]
    context = {
        "latest_threads": latest_threads,
    }
    return render(request, "boards/index.html", context)


def thread(request, post_id):
    response = f"You're looking at thread with id:{post_id}"
    return response

