from django.urls import re_path as url
# from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name='accounts'

urlpatterns = [ 
   url(r'^signup/$', views.signup_view, name='signup'),
   url(r'^login/$', views.login_view, name='login'),
   url(r'^logout/$', views.logout_view, name='logout')

]
