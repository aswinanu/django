from django.conf.urls import url, include
from django.contrib import admin
from registration.views import Home
from registration import urls as reg_urls

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^registration/',include(reg_urls)),
]
