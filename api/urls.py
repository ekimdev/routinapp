from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_routes),
    path("tasks/", views.get_tasks, name="tasks_api"),
    ]
