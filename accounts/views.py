from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic import TemplateView

from .forms import CreateUserForm
from django.contrib import messages


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('account:main')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                name = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + name)

                return redirect('account:login')

        context = {'form': form}
        return render(request, 'registr_page/registr.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('account:mainpage')
            else:
                messages.info(request, 'Username or Password wrong')
        context = {}
        return render(request, 'registr_page/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('account:mainpage')


# class DescriptionView(TemplateView):
