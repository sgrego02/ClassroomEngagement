# page/urls.py
from django.conf.urls import url
from page import views
# SET THE NAMESPACE!
app_name = 'page'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]