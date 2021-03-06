from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<id>[0-9]+)/$' , views.mainpage , name='index'),
    url(r'^(?P<id>[0-9]+)/financial/(?P<type>[\w\-]+)/$' , views.financial , name='financial'),
    url(r'^(?P<id>[0-9]+)/reservation/(?P<reserve>[0-9]+)/$', views.reservation, name='reservation'),
    url(r'^(?P<id>[0-9]+)/neighbors/$', views.neighbors, name='neighbors'),
    url(r'^(?P<id>[0-9]+)/guest/(?P<guest_id>[\w\-]+)/$', views.guest, name='guest'),
    url(r'^(?P<id>[0-9]+)/validation/$', views.validation, name='validation'),
    url(r'^(?P<id>[0-9]+)/owner/$', views.owner, name='owner'),


    #url(r'^$(?P<question_id>[0-9]+)/')
]