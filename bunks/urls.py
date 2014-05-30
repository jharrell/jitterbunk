from django.conf.urls import patterns, url

from bunks import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^bunk$', views.bunk, name='index'),
                       url(r'^(?P<user_id>\d+)/$',
                           views.detail,
                           name='detail'),
                       )
