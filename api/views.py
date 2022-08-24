from rest_framework.decorators import api_view
from rest_framework.response import Response, Serializer

from .serializers import TaskSerializer
from tasks.models import Task


@api_view(["GET"])
def get_routes(request):
    routes = [
        {"GET": "/api/tasks"},
        {"GET": "/api/tasks/id"},

        {"POST": "/api/users/token/"},
        {"POST": "/api/users/token/refresh"},
    ]

    return Response(routes)


@api_view(["GET"])
def get_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)
