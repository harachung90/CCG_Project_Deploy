from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from Account.forms import RegistrationForm, UserAuthenticationForm
from django.contrib import messages


def registration_view(request):
    context = {
        'navbar': 'register',
    }
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user = authenticate(email=email, password=raw_password, username=username, first_name=first_name,
                                last_name=last_name)
            login(request, user)
            return redirect('index')
        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'register.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')


def login_view(request):
    context = {
        'navbar': 'login',
    }

    user = request.user
    if user.is_authenticated:
        return redirect('index')

    if request.POST:
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('index')

    else:
        form = UserAuthenticationForm()

    context['login_form'] = form
    return render(request, 'login.html', context)
