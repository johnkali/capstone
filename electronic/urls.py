from django.conf.urls import url
from electronic import views
from electronic.views import UserFormView
app_name = 'electronic'


urlpatterns =[
    url(r'^$', views.show_login, name='index'),
    url(r'^login/$', views.login_user, name = 'login'),
    url(r'^home/$', views.show_home, name='home'),
    url(r'^logout/$', views.logout_user, name='logout_user'),
    url(r'^about/$', views.show_about, name='about'),
    url(r'^get_new_id/$', views.new_id, name='get_id'),
    url(r'^replace_id/$', views.replace_id, name='rep_id'),
    url(r'^id_status/$', views.id_status, name='id_stat'),
    url(r'^registration_form/$', UserFormView.as_view(), name='registration_form'),

]


