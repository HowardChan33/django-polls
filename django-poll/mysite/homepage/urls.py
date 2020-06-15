from sys import path

from django.conf.urls import url, include
import mysite
import polls
from . import views
from polls import urls

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'polls', polls.views.IndexView.as_view(), name='polls'),
]