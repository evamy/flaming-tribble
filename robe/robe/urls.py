"""robe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from tribble import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home' ),
    url(r'(?:.*?/)?(?P<path>(css|js|images)/.+)$', 'django.views.static.serve'),
    url(r'^explore/(?P<value>(India|Global))[/]$', views.trend , name='trend' ),
    url(r'^search/$', views.search , name='search' ),
    url(r'^search/(?P<value>(India|Global))/[.]*$', views.show , name='show' ),
    url(r'^statistics[?/]$', views.stats , name='stats' ),
    url(r'^live_trends/India[?/]$', views.fetch_india , name='india' ),
    url(r'^live_trends/Global[?/]$', views.fetch_global , name='global' ),
    url(r'^privacy[?/]$', views.privacy , name='privacy' ),
    url(r'^redundant_removal[?/]$', views.noRedundant , name='noRedundant' ),
]
