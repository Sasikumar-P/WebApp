from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
#    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'index/$',views.index, name='index'),
    url(r'new/$', views.new, name='new'),
    url(r'^author/$',views.author_list),
    url(r'^author/(?P<pk>[0-9]+)/$',views.author_detail),
    
]
