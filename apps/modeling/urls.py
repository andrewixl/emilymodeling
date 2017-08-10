from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^about$', views.about),
    url(r'^portfolio$', views.portfolio),
    url(r'^book$', views.book),
    url(r'^contact$', views.contact),
    url(r'^account$', views.account),
]
