from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from .models import FactionUser
# Uncomment below for view logging!
# import logging
# logger = logging.getLogger('testlogger')
# logger.info('This is a simple log message')

from .forms import UserForm


def register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True

        else:
            print user_form.errors

    else:
        user_form = UserForm()

    return render(request, 'registration/register.html',
                  context={
                      'user_form': user_form,
                      'registered': registered
                  }
                  )


def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        email = request.POST.get('email', '')
        username = FactionUser.objects.get(email=email).username
        password = request.POST.get('password', '')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(request.POST.get('next', '/'))
        else:
            return HttpResponse("Invalid login details supplied.")

    else:
        return render_to_response('registration/login.html', context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
