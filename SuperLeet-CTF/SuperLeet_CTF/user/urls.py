from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/', views.user_list, name='user_list'),
    url(r'^session/login/', views.login, name='login'),
    url(r'^session/signup/', views.signup, name='signup'),
]
