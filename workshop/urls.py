
from registration.views import Home
from django.conf.urls import include, url
from django.contrib import admin
from registration import urls as reg_urls
from workshop.views import anonymous_required
from registration.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^registration/',include(reg_urls)),
    url(r'^user/login/$',
        anonymous_required(auth_views.login),
        {'template_name': 'login.html'},
        name='login'),
    url(r'^user/logout/$',
        auth_views.logout,
        {'template_name': 'logout.html'},
        name='logout'),

]