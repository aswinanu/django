from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from registration import views
from registration.views import *
from registration.models import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', UserRegistrationView.as_view(), name='register_user'),
    url(r'^user/success/', TemplateView.as_view(template_name='sucess.html'),
        name='page'),
    url( r'^chocolate/add/', AddChocolateView.as_view(), name="add_chocolate"),
    url(r'^chocolate/list/', ListChocolateView.as_view(), name="list_chocolate")
]
