from django.urls import path

from . import views

app_name = "boards"
urlpatterns = [
    path("", views.index, name="index"),
    path("thread/<int:post_id>/", views.thread, name="thread")
]
