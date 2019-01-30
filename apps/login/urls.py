from django.conf.urls import url
from . import views
######################### LOGIN ###################
urlpatterns = [
    url(r'^$',views.index),
    url(r'^create$',views.create),
    url(r'^login$',views.login),
    url(r'^logout$', views.logout),
    url(r'^delete/(?P<id>[0-9]+)$',views.delete),
]