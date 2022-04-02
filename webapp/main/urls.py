from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.registerPage, name="register"),
	path(r'^login/$', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    url(r'^$', views.home, name='home'),
    url(r'^consult/$', views.consult, name='consult'),
    url(r'^management/$', views.management, name='management'),
    url(r'^market/$', views.market, name='market'),
    url(r'^monitoring/$', views.monitoring, name='monitoring'),
    url(r'^investment/$', views.investment, name='investment'),


]
