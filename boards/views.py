from django.shortcuts import get_object_or_404, render

from .models import Thread


def index(request):
    latest_threads = Thread.objects.order_by("-creation_datetime")[:5]
    context = {
        "latest_threads": latest_threads,
    }
    return render(request, "boards/index.html", context)


def thread(request, post_id):
    thread = get_object_or_404(Thread, pk=post_id)
    return render(request, "boards/thread.html", {"thread": thread})

