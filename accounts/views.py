from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from .forms import CreateUserForm
from django.contrib import messages


def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('username')
            messages.success(request, 'Account created as ' + name)
            return redirect('login')

    context = {'form': form}
    return render(request, 'registr_page/registr.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('mainpage')
        else:
            messages.info(request, 'Username or Password wrong')

    context = {}
    return render(request, 'registr_page/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('mainpage')
