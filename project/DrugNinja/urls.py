from django.conf.urls import patterns, url

from DrugNinja import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
)
