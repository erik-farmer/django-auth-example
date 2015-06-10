from django.conf.urls import url
from .views import register
from .views import user_login
from .views import user_logout

urlpatterns = [
    url(r'^register/$', register),
    url(r'^login/', user_login),
    url(r'^logout/$', user_logout),
]
