from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from .forms import CustomUserCreationForm


def login_user(request):
    page = "login"
    form = AuthenticationForm()

    if request.user.is_authenticated:
        return redirect("tasks")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # user = User.objects.get(username=username)

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                print("se pudo")
                return redirect("tasks")
            else:
                print("No se pudo")
        else:
            print("form no valido")

    context = {"page": page, "form": form}
    return render(request, "users/login_register.html", context)


def logout_user(request):
    logout(request)
    return redirect('login')


def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            return redirect('tasks')

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)


def account(request):
    return render(request, "account.html")
