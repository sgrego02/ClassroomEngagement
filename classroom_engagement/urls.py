# classroom_engagement/urls.py
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from page import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^page/',include('page.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^features/$',views.features,name='features'),
    url(r'^tools$',views.tools,name='tools'),
    url(r'^history$',views.history,name='history'),
]

urlpatterns += staticfiles_urlpatterns()