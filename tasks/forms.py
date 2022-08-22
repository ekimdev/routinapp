from django.forms import ModelForm
from django import forms

from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "tags"]
        widgets = {
                "tags": forms.CheckboxSelectMultiple(),
                }
