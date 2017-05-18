from django.conf.urls import url
from electronic import views

urlpatterns =[
    url(r'^$', views.show_login, name='index'),
    url(r'^login/$', views.login_user, name = 'login'),
    url(r'^home/$', views.show_home, name='home'),
    url(r'^logout/$', views.logout_user, name='logout_user'),
]


