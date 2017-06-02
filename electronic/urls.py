from django.conf.urls import url
from electronic import views
#from electronic.views import UserFormView
app_name = 'electronic'


urlpatterns =[
    url(r'^$', views.show_login, name='index'),
    url(r'^login/$', views.login_user, name = 'login'),
    url(r'^home/$', views.show_home, name='home'),
    url(r'^logout/$', views.logout_user, name='logout_user'),
    url(r'^about/$', views.show_about, name='about'),
    url(r'^get_new_id/$', views.new_id, name='get_id'),
   #url(r'^replace_id/$', views.replace_id, name='rep_id'),
    url(r'^id_status/$', views.id_status, name='id_stat'),
    url(r'^registration_form/$', views.registration_form, name='registration_form'),
    url(r'^do_register/$', views.do_register, name = 'do_register'),
    url(r'^account_register/$', views.account_register, name='account_register'),
    url(r'^get_id_info/$', views.get_id_info, name='get_id_info'),
    url(r'^do_replace/$', views.do_replace, name='do_replace'),

]


