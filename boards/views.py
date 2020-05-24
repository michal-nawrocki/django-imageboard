from django.http import HttpResponse

from .models import Thread, Post


def index(request):
    latest_threads = Thread.objects.order_by("-creation_datetime")[:5]
    output = ', '.join([t.text for t in latest_threads])
    return HttpResponse(output)


def thread(request, post_id):
    response = f"You're looking at thread with id:{post_id}"
    return response

