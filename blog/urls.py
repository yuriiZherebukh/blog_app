"""application URL Configuration

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
from django.conf.urls import url
from .views import PostView

urlpatterns = [

    url(r'^$', PostView.as_view(), name='post_view'),
    url(r'^post/(?P<post_id>\d+)/$', PostView.as_view(), name='post_describe'),
    url(r'^post/new/$', PostView.as_view(), name='post_new'),
    url(r'^post/(?P<post_id>\d+)/edit/$', PostView.as_view(), name='post_edit'),
    url(r'^post/(?P<post_id>\d+)/delete/$', PostView.as_view(), name='post_elete'),
]
