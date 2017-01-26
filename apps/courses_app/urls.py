from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index), # you were missing a dollar sign for the root route. it was executing the same logic in index instead of add_course
    url(r'^course_add$', views.course_add),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^deleteForRealz/(?P<id>\d+)$', views.deleteForRealz)
]
