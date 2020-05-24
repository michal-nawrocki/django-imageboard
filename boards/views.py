from django.shortcuts import get_object_or_404, render

from .models import ThreadEntry


def index(request):
    latest_threads = ThreadEntry.objects.order_by("-creation_datetime")[:5]
    return render(request, "boards/index.html", {"latest_threads": latest_threads})


def thread(request, post_id):
    thread_entry = get_object_or_404(ThreadEntry, pk=post_id)
    return render(request, "boards/thread.html", {"thread": thread_entry})

