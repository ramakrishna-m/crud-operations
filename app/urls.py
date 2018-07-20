from django.conf.urls import url
from . import views

app_name='app'

urlpatterns = [
    url(r'^$',views.index),
    url(r'^reg$',views.sign_up_form),
    url(r'^login$',views.login_form),
    url(r'^delete',views.delete_form),
    url(r'^details/',views.details),
]