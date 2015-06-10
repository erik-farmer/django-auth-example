from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
import logging
logger = logging.getLogger('testlogger')
logger.info('This is a simple log message')

from .forms import UserForm, UserProfileForm


def register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            # This step hashes the password
            # TODO Look into Bcrypt
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'registration/register.html',
                  context={
                      'user_form': user_form,
                      'profile_form': profile_form,
                      'registered': registered
                  }
                  )


def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

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
