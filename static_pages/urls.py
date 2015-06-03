from django.conf.urls import url
from .views import HomePageView
from .views import ProtectedView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^protected$', login_required(ProtectedView.as_view(), login_url='/login/'), name='protected'),
]
