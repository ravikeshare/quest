"""quest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework import routers
from django.conf.urls import include, url
from django.views.generic import RedirectView

from quest.qa.api import QuestionViewSet

router = routers.DefaultRouter()
router.register(r'qa/(?P<key>[0-9]{6})', QuestionViewSet, base_name='qa')


urlpatterns = [
    url(r'^api/v1/', include(router.urls, namespace='api-v1')),
    url(r'^api/$', RedirectView.as_view(url='/api/v1/'), name='redirect-api-version'),
    url(r'^admin/', admin.site.urls),
]
