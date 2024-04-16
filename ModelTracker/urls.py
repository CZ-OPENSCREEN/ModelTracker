# from django.conf.urls import url,re_path
from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path('^$',views.main,name="main"),
    path('show/',views.showChanges,name="showModelChanges"),
    re_path(r'revert/(\d+)',views.revert,name="revert"),
    path('get/',views.getChanges,name="getModelChanges"),
]
