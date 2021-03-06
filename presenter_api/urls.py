"""presenter_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from server.presenter_webapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^proteindataviz/$', views.PresenterDataVizList.as_view()),
    url(r'^proteindataviz/(?P<pk>[0-9]+)$', views.PresenterDataVizDetail.as_view()),
    url(r'^datavizfile/(?P<pk>[0-9]+)$', views.PresenterViz.as_view()),
    url(r'^viewviz/(?P<pk>[0-9]+)$', views.ViewViz.as_view()),
    url(r'^allposts/$', views.AllPosts.as_view()),
    url(r'^retriever/$', views.post_simple),
]

urlpatterns = format_suffix_patterns(urlpatterns)
