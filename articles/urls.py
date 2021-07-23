from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url

app_name = "articles"

urlpatterns = [
    path('', views.article_list, name="list"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
]
