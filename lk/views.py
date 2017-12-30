from lk.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as dj_login
from django.contrib.auth import logout as dj_logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate

# Create your views here.

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/login/')
    else:
        form = RegistrationForm()

    return render(request,
    'register.html',
    {'form': form}
    )


def logout(request):
    dj_logout(request)
    return redirect('/login/')


@csrf_protect
def login(request):
    dj_logout(request)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                dj_login(request, user)
                return HttpResponseRedirect('/feed/')
            return render(request,
            'login.html',
            {'form': form, 'alert': 'Такого пользователя нет'}
            )
    else:
        form = LoginForm()

    return render(request,
    'login.html',
    {'form': form}
    )
