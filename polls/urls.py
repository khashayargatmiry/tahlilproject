from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<id>[0-9]+)/$' , views.mainpage),
    url(r'^(?P<id>[0-9]+)/financial/$' , views.financial , name='financial')
    #url(r'^$(?P<question_id>[0-9]+)/')
]