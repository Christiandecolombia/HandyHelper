from django.conf.urls import url
from . import views
######################### HANDYHELPER ###################
urlpatterns = [
    url(r'^mainpage$',views.mainpage),
    url(r'^addjob$',views.addjob),
    url(r'^createjob$',views.createjob),
    url(r'^viewjob/(?P<id>[0-9]+)$',views.viewjob),
    url(r'^editjob/(?P<id>[0-9]+)$',views.editjob),
    url(r'^edit/(?P<id>[0-9]+)$',views.edit),
    url(r'^deletejob/(?P<id>[0-9]+)$',views.deletejob),
    url(r'^logout$', views.logout),
]