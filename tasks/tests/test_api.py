import json

from django.test import TestCase
from django.urls import reverse

from tasks.models import Task


class TaskAPITestCase(TestCase):

    def setUp(self):
        Task.objects.get_or_create(
            title="Write tests",
            description="Write tests for this app jeje"
        )

    def test_list(self):
        url = reverse("tasks_api")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEquals(len(data), 1)
        title = data[0]["title"]
        self.assertEquals("Write tests", title)
